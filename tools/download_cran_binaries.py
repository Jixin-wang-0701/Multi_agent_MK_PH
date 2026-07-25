from __future__ import annotations

import argparse
from collections import defaultdict, deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import re
import sys
import urllib.request


BASE_PACKAGES = {
    "base",
    "compiler",
    "datasets",
    "graphics",
    "grDevices",
    "grid",
    "methods",
    "parallel",
    "splines",
    "stats",
    "stats4",
    "tcltk",
    "tools",
    "utils",
    "R",
}

DEPENDENCY_FIELDS = ("Depends", "Imports", "LinkingTo")


def read_url(url: str) -> str:
    with urllib.request.urlopen(url, timeout=60) as response:
        return response.read().decode("utf-8", errors="replace")


def parse_dcf(text: str) -> dict[str, dict[str, str]]:
    records: dict[str, dict[str, str]] = {}
    current: dict[str, str] = {}
    last_key: str | None = None
    for raw_line in text.splitlines():
        line = raw_line.rstrip("\r")
        if not line:
            if current.get("Package"):
                records[current["Package"]] = current
            current = {}
            last_key = None
            continue
        if line.startswith((" ", "\t")) and last_key:
            current[last_key] += " " + line.strip()
            continue
        key, sep, value = line.partition(":")
        if sep:
            current[key] = value.strip()
            last_key = key
    if current.get("Package"):
        records[current["Package"]] = current
    return records


def dependency_names(record: dict[str, str]) -> set[str]:
    names: set[str] = set()
    for field in DEPENDENCY_FIELDS:
        value = record.get(field, "")
        for part in value.split(","):
            name = re.sub(r"\s*\(.*?\)", "", part).strip()
            if name and name not in BASE_PACKAGES and not name.startswith("R "):
                names.add(name)
    return names


def resolve(records: dict[str, dict[str, str]], roots: list[str]) -> list[str]:
    needed: set[str] = set()
    visiting: deque[str] = deque(roots)
    missing: set[str] = set()
    while visiting:
        package = visiting.popleft()
        if package in BASE_PACKAGES or package in needed:
            continue
        record = records.get(package)
        if not record:
            missing.add(package)
            continue
        needed.add(package)
        for dep in dependency_names(record):
            if dep not in needed:
                visiting.append(dep)
    if missing:
        raise RuntimeError(f"Packages not found in CRAN binary index: {', '.join(sorted(missing))}")

    graph: dict[str, set[str]] = {}
    reverse: dict[str, set[str]] = defaultdict(set)
    for package in needed:
        deps = {dep for dep in dependency_names(records[package]) if dep in needed}
        graph[package] = deps
        for dep in deps:
            reverse[dep].add(package)

    ready = deque(sorted(package for package, deps in graph.items() if not deps))
    ordered: list[str] = []
    while ready:
        package = ready.popleft()
        ordered.append(package)
        for dependent in sorted(reverse[package]):
            graph[dependent].discard(package)
            if not graph[dependent]:
                ready.append(dependent)
    if len(ordered) != len(needed):
        unresolved = sorted(set(needed) - set(ordered))
        raise RuntimeError(f"Dependency cycle or unresolved ordering: {', '.join(unresolved)}")
    return ordered


def download_package(repo: str, record: dict[str, str], output_dir: Path) -> Path:
    package = record["Package"]
    version = record["Version"]
    filename = f"{package}_{version}.zip"
    target = output_dir / filename
    if target.exists() and target.stat().st_size > 0:
        return target
    url = f"{repo.rstrip('/')}/{filename}"
    print(f"Downloading {filename}", flush=True)
    with urllib.request.urlopen(url, timeout=180) as response:
        target.write_bytes(response.read())
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description="Download CRAN Windows binary packages and dependencies.")
    parser.add_argument("--repo", default="https://cloud.r-project.org/bin/windows/contrib/4.6")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("packages", nargs="+")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    index_text = read_url(f"{args.repo.rstrip('/')}/PACKAGES")
    records = parse_dcf(index_text)
    ordered = resolve(records, args.packages)
    manifest = output_dir / "install_order.txt"
    package_paths = {
        package: output_dir / f"{package}_{records[package]['Version']}.zip"
        for package in ordered
    }
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {
            executor.submit(download_package, args.repo, records[package], output_dir): package
            for package in ordered
        }
        for future in as_completed(futures):
            future.result()
    paths = [package_paths[package] for package in ordered]
    manifest.write_text("\n".join(str(path.resolve()) for path in paths) + "\n", encoding="utf-8")
    print(f"Resolved {len(paths)} packages.")
    print(f"Install order: {manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
