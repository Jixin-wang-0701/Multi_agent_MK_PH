from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os
import re
import shutil
import subprocess


WANTED_R_PACKAGES = [
    "Seurat",
    "SeuratObject",
    "Matrix",
    "dplyr",
    "readr",
    "jsonlite",
    "future",
    "ggplot2",
]


@dataclass(frozen=True)
class RScriptCandidate:
    path: Path
    version: str
    ok: bool
    detail: str


@dataclass(frozen=True)
class RDiagnostics:
    selected: Path | None
    candidates: list[RScriptCandidate]
    lib_paths: list[str]
    packages: dict[str, bool]
    raw_output: str


def discover_rscript_candidates() -> list[Path]:
    candidates: list[Path] = []

    env_path = os.environ.get("RSCRIPT_PATH")
    if env_path:
        candidates.append(Path(env_path))

    which_path = shutil.which("Rscript")
    if which_path:
        candidates.append(Path(which_path))

    candidates.extend(_glob_paths(r"C:\Program Files\R\R-*\bin\x64\Rscript.exe"))
    candidates.extend(_glob_paths(r"C:\Program Files\R\R-*\bin\Rscript.exe"))
    candidates.extend(_glob_paths(r"C:\Program Files (x86)\R\R-*\bin\x64\Rscript.exe"))
    candidates.extend(_glob_paths(r"C:\Program Files (x86)\R\R-*\bin\Rscript.exe"))

    userprofile = Path(os.environ.get("USERPROFILE", str(Path.home())))
    candidates.extend(_glob_paths(str(userprofile / "anaconda3" / "envs" / "*" / "Scripts" / "Rscript.exe")))
    candidates.extend(_glob_paths(str(userprofile / "anaconda3" / "envs" / "*" / "Library" / "bin" / "Rscript.exe")))
    candidates.extend(_glob_paths(str(userprofile / "anaconda3" / "pkgs" / "r-base-*" / "Scripts" / "Rscript.exe")))

    deduped: list[Path] = []
    seen: set[str] = set()
    for candidate in candidates:
        normalized = str(candidate).lower()
        if normalized in seen:
            continue
        seen.add(normalized)
        deduped.append(candidate)
    return deduped


def _glob_paths(pattern: str) -> list[Path]:
    import glob

    return [Path(path) for path in glob.glob(pattern)]


def evaluate_rscript(path: Path, timeout_seconds: int = 15) -> RScriptCandidate:
    if not path.exists():
        return RScriptCandidate(path=path, version="", ok=False, detail="path does not exist")
    try:
        result = subprocess.run(
            [str(path), "--version"],
            text=True,
            capture_output=True,
            timeout=timeout_seconds,
            check=False,
        )
    except Exception as exc:  # noqa: BLE001 - report exact local runtime issue.
        return RScriptCandidate(path=path, version="", ok=False, detail=str(exc))

    output = (result.stdout + "\n" + result.stderr).strip()
    match = re.search(r"version\s+([0-9]+(?:\.[0-9]+)+)", output)
    version = match.group(1) if match else ""
    return RScriptCandidate(
        path=path,
        version=version,
        ok=result.returncode == 0 and bool(version),
        detail=output or f"return code {result.returncode}",
    )


def select_rscript() -> Path | None:
    candidates = [evaluate_rscript(path) for path in discover_rscript_candidates()]
    usable = [candidate for candidate in candidates if candidate.ok]
    if not usable:
        return None

    usable.sort(
        key=lambda candidate: (
            0 if "\\pkgs\\" in str(candidate.path).lower() else 1,
            1 if "\\x64\\" in str(candidate.path).lower() else 0,
            _version_tuple(candidate.version),
        ),
        reverse=True,
    )
    return usable[0].path


def _version_tuple(version: str) -> tuple[int, ...]:
    return tuple(int(part) for part in re.findall(r"\d+", version))


def r_diagnostics() -> RDiagnostics:
    candidate_reports = [evaluate_rscript(path) for path in discover_rscript_candidates()]
    selected = select_rscript()
    if not selected:
        return RDiagnostics(
            selected=None,
            candidates=candidate_reports,
            lib_paths=[],
            packages={name: False for name in WANTED_R_PACKAGES},
            raw_output="No usable Rscript found.",
        )

    expression = """
cat("version\\t", as.character(getRversion()), "\\n", sep = "")
cat("home\\t", R.home(), "\\n", sep = "")
cat("lib_paths\\t", paste(.libPaths(), collapse = "|"), "\\n", sep = "")
cat("r_libs_user\\t", Sys.getenv("R_LIBS_USER"), "\\n", sep = "")
pk <- rownames(installed.packages())
wanted <- strsplit(Sys.getenv("MULTI_AGENT_R_PACKAGES"), ",", fixed = TRUE)[[1]]
for (pkg in wanted) {
  cat("package\\t", pkg, "\\t", pkg %in% pk, "\\n", sep = "")
}
""".strip()
    result = subprocess.run(
        [str(selected), "-e", expression],
        text=True,
        capture_output=True,
        timeout=30,
        check=False,
        env={**os.environ, "MULTI_AGENT_R_PACKAGES": ",".join(WANTED_R_PACKAGES)},
    )
    raw_output = (result.stdout + "\n" + result.stderr).strip()
    lib_paths: list[str] = []
    packages = {name: False for name in WANTED_R_PACKAGES}
    for line in result.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) >= 2 and parts[0] == "lib_paths":
            lib_paths = [item for item in parts[1].split("|") if item]
        if len(parts) >= 3 and parts[0] == "package":
            packages[parts[1]] = parts[2].strip().upper() == "TRUE"
    return RDiagnostics(
        selected=selected,
        candidates=candidate_reports,
        lib_paths=lib_paths,
        packages=packages,
        raw_output=raw_output,
    )


def diagnostics_markdown() -> str:
    diagnostics = r_diagnostics()
    lines = ["# R Environment Diagnostics", ""]
    lines.append(f"Selected Rscript: {diagnostics.selected or 'None'}")
    lines.extend(["", "## Candidates"])
    if not diagnostics.candidates:
        lines.append("- No candidates discovered.")
    for candidate in diagnostics.candidates:
        status = "OK" if candidate.ok else "FAILED"
        version = candidate.version or "unknown"
        lines.append(f"- {status}: {candidate.path} (version: {version})")
    lines.extend(["", "## Library Paths"])
    if diagnostics.lib_paths:
        lines.extend(f"- {path}" for path in diagnostics.lib_paths)
    else:
        lines.append("- None detected.")
    lines.extend(["", "## Package Availability"])
    for name, available in diagnostics.packages.items():
        lines.append(f"- {name}: {'available' if available else 'missing'}")
    return "\n".join(lines).strip() + "\n"


def summarize_rds_with_r(rds_path: Path, script_path: Path, timeout_seconds: int = 600) -> str:
    rscript = select_rscript()
    if not rscript:
        return (
            "Rscript was not found. The RDS file is present, but direct Seurat inspection is disabled."
        )
    if not script_path.exists():
        return f"Rscript is available at {rscript}, but the R summarizer script is missing: {script_path}"

    result = subprocess.run(
        [str(rscript), str(script_path), str(rds_path)],
        text=True,
        capture_output=True,
        timeout=timeout_seconds,
        check=False,
        env={**os.environ, "MULTI_AGENT_R_PACKAGES": ",".join(WANTED_R_PACKAGES)},
    )
    output = result.stdout.strip()
    errors = result.stderr.strip()
    if result.returncode != 0:
        return (
            f"Rscript failed while summarizing {rds_path.name}.\n"
            f"- Rscript: {rscript}\n"
            f"- Return code: {result.returncode}\n"
            f"- stdout:\n{output or '[empty]'}\n"
            f"- stderr:\n{errors or '[empty]'}"
        )
    if errors:
        output += f"\n\nR stderr notes:\n{errors}"
    return output.strip() or "Rscript completed but produced no summary."
