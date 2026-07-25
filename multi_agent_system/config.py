from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os
import sys
from typing import Iterable


PROMPT_FILES = {
    "pi": "PI_agent_gpt.txt",
    "generation": "generationg_agent_gpt.txt",
    "generation_runtime": "generation_runtime_agent_gpt.txt",
    "proximity": "proximity_agent_gt.txt",
    "reflection": "reflection_agent_gpt.txt",
    "ranking": "ranking_agent_gpt.txt",
    "meta_review": "meta_review_agent_gpt.txt",
    "evolution": "evolution_agent_gpt.txt",
    "tool_use": "tool_use_agent_gpt.txt",
    "public_dataset": "public_dataset_agent_gpt.txt",
}

TEMPLATE_FILES = {
    "pi_to_generation": "PI_TO_GENERATION_BRIEF.txt",
    "generation_to_pi": "GENERATION_TO_PI_OUTPUT.txt",
}

DATA_FILES = {
    "single_cell_rds": "seurat_merged.rds",
    "mk_metabolomics": "sFig6A Raw data.xlsx",
    "ph_control_metabolomics": "Figure6D+F raw data.xlsx",
    "prior_results": "prior_results.docx",
}


@dataclass(frozen=True)
class SystemConfig:
    root: Path
    output_dir: Path
    api_key: str | None
    model: str
    fallback_model: str | None
    thinking: str
    reasoning_effort: str | None
    base_url: str
    timeout_seconds: int
    max_tokens: int
    generation_max_tokens: int
    pi_max_tokens: int
    dry_run: bool = False

    @property
    def has_api_key(self) -> bool:
        if not self.api_key or not self.api_key.strip():
            return False
        value = self.api_key.strip().lower()
        placeholder_fragments = ("replace_with", "your_key", "your-api-key", "your_deepseek")
        return not any(fragment in value for fragment in placeholder_fragments)


@dataclass(frozen=True)
class CheckItem:
    name: str
    ok: bool
    detail: str


def load_env_file(env_file: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not env_file.exists():
        return values
    for raw_line in env_file.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            values[key] = value
    return values


def get_setting(name: str, env_values: dict[str, str], default: str | None = None) -> str | None:
    return os.environ.get(name) or env_values.get(name) or default


def make_config(
    root: Path,
    output_dir: Path | None = None,
    env_file: Path | None = None,
    dry_run: bool = False,
) -> SystemConfig:
    env_path = env_file or root / ".env"
    env_values = load_env_file(env_path)
    apply_runtime_env(env_values)
    apply_workspace_python_packages()
    apply_workspace_r_libs(root)
    return SystemConfig(
        root=root,
        output_dir=output_dir or root / "outputs",
        api_key=get_setting("DEEPSEEK_API_KEY", env_values),
        model=get_setting("DEEPSEEK_MODEL", env_values, "deepseek-v4-pro") or "deepseek-v4-pro",
        fallback_model=get_setting("DEEPSEEK_FALLBACK_MODEL", env_values, "deepseek-v4-flash"),
        thinking=get_setting("DEEPSEEK_THINKING", env_values, "enabled") or "enabled",
        reasoning_effort=get_setting("DEEPSEEK_REASONING_EFFORT", env_values),
        base_url=get_setting("DEEPSEEK_BASE_URL", env_values, "https://api.deepseek.com")
        or "https://api.deepseek.com",
        timeout_seconds=int(get_setting("DEEPSEEK_TIMEOUT_SECONDS", env_values, "120") or "120"),
        max_tokens=int(get_setting("DEEPSEEK_MAX_TOKENS", env_values, "4096") or "4096"),
        generation_max_tokens=int(get_setting("DEEPSEEK_GENERATION_MAX_TOKENS", env_values, "65536") or "65536"),
        pi_max_tokens=int(get_setting("DEEPSEEK_PI_MAX_TOKENS", env_values, "16384") or "16384"),
        dry_run=dry_run,
    )


def apply_runtime_env(env_values: dict[str, str]) -> None:
    for key in ("RSCRIPT_PATH", "R_LIBS", "R_LIBS_USER", "R_LIBS_SITE"):
        value = env_values.get(key)
        if value and not os.environ.get(key):
            os.environ[key] = value


def apply_workspace_python_packages() -> None:
    bundled_site_packages = (
        Path.home()
        / ".cache"
        / "codex-runtimes"
        / "codex-primary-runtime"
        / "dependencies"
        / "python"
        / "Lib"
        / "site-packages"
    )
    if bundled_site_packages.exists():
        path_text = str(bundled_site_packages)
        if path_text not in sys.path:
            sys.path.append(path_text)


def apply_workspace_r_libs(root: Path) -> None:
    library_root = root / "r_library"
    if not library_root.exists():
        return
    libraries = [path for path in sorted(library_root.iterdir()) if path.is_dir()]
    if not libraries:
        return
    separator = ";" if os.name == "nt" else ":"
    existing = os.environ.get("R_LIBS")
    library_value = separator.join(str(path) for path in libraries)
    if existing:
        os.environ["R_LIBS"] = library_value + separator + existing
    else:
        os.environ["R_LIBS"] = library_value


def missing_files(root: Path, filenames: Iterable[str]) -> list[str]:
    return [name for name in filenames if not (root / name).exists()]


def doctor(config: SystemConfig) -> list[CheckItem]:
    root = config.root
    checks: list[CheckItem] = []

    prompt_missing = missing_files(root, PROMPT_FILES.values())
    checks.append(
        CheckItem(
            "agent prompts",
            not prompt_missing,
            "all prompt files found" if not prompt_missing else "missing: " + ", ".join(prompt_missing),
        )
    )

    template_missing = missing_files(root, TEMPLATE_FILES.values())
    checks.append(
        CheckItem(
            "handoff templates",
            not template_missing,
            "all template files found"
            if not template_missing
            else "missing: " + ", ".join(template_missing),
        )
    )

    data_missing = missing_files(root, DATA_FILES.values())
    checks.append(
        CheckItem(
            "user data files",
            not data_missing,
            "all expected data files found" if not data_missing else "missing: " + ", ".join(data_missing),
        )
    )

    checks.append(
        CheckItem(
            "DeepSeek API key",
            config.dry_run or config.has_api_key,
            "configured" if config.has_api_key else "not configured; dry-run mode can still be used",
        )
    )

    checks.append(
        CheckItem(
            "output directory",
            True,
            str(config.output_dir),
        )
    )

    return checks


def read_required_text(root: Path, filename: str) -> str:
    path = root / filename
    if not path.exists():
        raise FileNotFoundError(f"Required file is missing: {path}")
    return path.read_text(encoding="utf-8")
