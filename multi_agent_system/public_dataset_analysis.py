from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import csv
import gzip
import html.parser
import json
import math
import re
import shutil
import subprocess
import tarfile
import urllib.parse
import urllib.request

try:
    import numpy as np
    import pandas as pd
except ModuleNotFoundError:
    np = None
    pd = None

from .public_dataset_context import md_escape, shorten, url_get


CANDIDATE_GENES = [
    "AMD1",
    "AMD2",
    "DNMT3B",
    "CYP26B1",
    "VEGFA",
    "IL6",
    "TGFB1",
    "COL1A1",
    "ACTA2",
    "MYH11",
    "PECAM1",
    "VWF",
    "PF4",
    "PPBP",
    "ITGA2B",
    "MMP9",
    "CXCL12",
    "HIF1A",
]

SUPPORTED_TABLE_SUFFIXES = (
    ".txt",
    ".tsv",
    ".csv",
    ".mtx",
    ".txt.gz",
    ".tsv.gz",
    ".csv.gz",
    ".mtx.gz",
    ".xlsx",
    ".xls",
)

SKIP_SUFFIXES = (
    ".fastq",
    ".fq",
    ".fastq.gz",
    ".fq.gz",
    ".bam",
    ".sam",
    ".sra",
    ".cram",
    ".bw",
    ".bigwig",
)


@dataclass
class GeoSummary:
    accession: str
    title: str
    organism: str
    modality: str
    ftplink: str
    suppfile: str
    samples: list[dict[str, str]]


@dataclass
class AnalysisResult:
    accession: str
    status: str
    reason: str
    matrix_file: str = ""
    n_genes: int = 0
    n_samples: int = 0
    comparison: str = ""
    candidate_gene_path: str = ""
    de_results_path: str = ""
    report_path: str = ""


class LinkParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        for key, value in attrs:
            if key.lower() == "href" and value:
                self.links.append(value)


def build_public_dataset_analysis_context(
    root: Path,
    output_dir: Path,
    *,
    enabled: bool = False,
    max_datasets: int = 3,
    max_download_mb: int = 300,
    force: bool = False,
    accessions: list[str] | None = None,
    reuse_existing_only: bool = False,
) -> Path:
    analysis_dir = output_dir / "public_dataset_analysis"
    analysis_dir.mkdir(parents=True, exist_ok=True)
    public_dir = output_dir / "public_datasets"
    hits_path = public_dir / "public_dataset_hits.csv"
    context_path = output_dir / "public_dataset_analysis_context.md"
    generated_at = datetime.now().isoformat(timespec="seconds")

    if not enabled:
        manifest = {
            "generated_at": generated_at,
            "enabled": False,
            "results": [],
            "access_issues": ["Public dataset analysis disabled by runtime option."],
        }
        (analysis_dir / "public_dataset_analysis_manifest.json").write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        context_path.write_text(format_analysis_context([], manifest), encoding="utf-8")
        return context_path

    if not reuse_existing_only:
        ensure_analysis_dependencies()

    if not hits_path.exists():
        results = collect_existing_analysis_results(analysis_dir, max_results=max_datasets)
        manifest = {
            "generated_at": generated_at,
            "enabled": enabled,
            "reuse_existing_only": reuse_existing_only,
            "results": [result.__dict__ for result in results],
            "access_issues": [f"Missing public dataset hits CSV: {hits_path}"] if not results else [],
        }
        (analysis_dir / "public_dataset_analysis_manifest.json").write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        context_path.write_text(format_analysis_context(results, manifest), encoding="utf-8")
        return context_path

    summaries = load_geo_summaries(public_dir / "cache")
    hits = read_hits(hits_path)
    selected = [] if reuse_existing_only else select_analysis_ready_hits(
        hits,
        summaries,
        max_datasets=max(max_datasets * 4, max_datasets + 5),
        accessions=accessions,
    )
    results: list[AnalysisResult] = []
    access_issues: list[str] = []
    completed_count = 0

    for hit in selected:
        if completed_count >= max_datasets:
            break
        accession = hit.get("accession", "")
        summary = summaries.get(accession)
        if not summary:
            results.append(AnalysisResult(accession, "skipped", "No cached GEO summary metadata found."))
            continue
        try:
            result = analyze_geo_dataset(
                summary,
                analysis_dir / accession,
                max_download_mb=max_download_mb,
                force=force,
            )
        except Exception as exc:
            result = AnalysisResult(accession, "failed", f"{type(exc).__name__}: {exc}")
            access_issues.append(f"{accession}: {type(exc).__name__}: {exc}")
        results.append(result)
        if result.status == "completed":
            completed_count += 1
    if completed_count < max_datasets:
        existing = collect_existing_analysis_results(
            analysis_dir,
            max_results=max_datasets - completed_count,
            exclude_accessions={result.accession for result in results},
        )
        results.extend(existing)

    manifest = {
        "generated_at": generated_at,
        "enabled": enabled,
        "reuse_existing_only": reuse_existing_only,
        "max_datasets": max_datasets,
        "max_download_mb": max_download_mb,
        "requested_accessions": accessions or [],
        "results": [result.__dict__ for result in results],
        "access_issues": access_issues,
    }
    (analysis_dir / "public_dataset_analysis_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    context_path.write_text(format_analysis_context(results, manifest), encoding="utf-8")
    return context_path


def collect_existing_analysis_results(
    analysis_dir: Path,
    *,
    max_results: int,
    exclude_accessions: set[str] | None = None,
) -> list[AnalysisResult]:
    exclude = exclude_accessions or set()
    results: list[AnalysisResult] = []
    if max_results <= 0 or not analysis_dir.exists():
        return results
    for report_path in sorted(analysis_dir.glob("GSE*/analysis_report.md")):
        accession = report_path.parent.name
        if accession in exclude:
            continue
        result = parse_existing_analysis_report(report_path)
        if result and result.status == "completed":
            results.append(result)
        if len(results) >= max_results:
            break
    return results


def parse_existing_analysis_report(report_path: Path) -> AnalysisResult | None:
    text = report_path.read_text(encoding="utf-8", errors="replace")
    accession = report_path.parent.name
    status = report_field(text, "Status")
    if not status:
        return None
    genes, samples = parse_genes_samples(report_field(text, "Genes x samples"))
    return AnalysisResult(
        accession=accession,
        status=status,
        reason=report_field(text, "Reason") or "Existing processed-matrix analysis indexed from saved report.",
        matrix_file=report_field(text, "Matrix file"),
        n_genes=genes,
        n_samples=samples,
        comparison=report_field(text, "Comparison"),
        candidate_gene_path=report_field(text, "Candidate gene check"),
        de_results_path=report_field(text, "Differential analysis"),
        report_path=str(report_path),
    )


def report_field(text: str, field: str) -> str:
    match = re.search(rf"^- {re.escape(field)}:\s*(.+)$", text, flags=re.MULTILINE)
    if not match:
        return ""
    value = match.group(1).strip()
    return "" if value.lower() in {"none", "not available"} else value


def parse_genes_samples(value: str) -> tuple[int, int]:
    match = re.search(r"(\d+)\s*x\s*(\d+)", value)
    if not match:
        return 0, 0
    return int(match.group(1)), int(match.group(2))


def read_hits(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def ensure_analysis_dependencies() -> None:
    missing = []
    if pd is None:
        missing.append("pandas")
    if np is None:
        missing.append("numpy")
    if missing:
        raise RuntimeError(
            "Public dataset analysis requires " + ", ".join(missing) + ". "
            "Use the bundled workspace Python runtime or install these packages in the active Python environment."
        )


def load_geo_summaries(cache_dir: Path) -> dict[str, GeoSummary]:
    summaries: dict[str, GeoSummary] = {}
    if not cache_dir.exists():
        return summaries
    for path in cache_dir.glob("geo_summary_*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        result = data.get("result", {})
        for uid in result.get("uids", []):
            item = result.get(uid, {})
            accession = str(item.get("accession") or "")
            if not accession.startswith("GSE"):
                continue
            title = str(item.get("title") or accession)
            modality = infer_modality_from_geo(item)
            summaries[accession] = GeoSummary(
                accession=accession,
                title=title,
                organism=str(item.get("taxon") or ""),
                modality=modality,
                ftplink=str(item.get("ftplink") or ""),
                suppfile=str(item.get("suppfile") or ""),
                samples=[
                    {"accession": str(sample.get("accession") or ""), "title": str(sample.get("title") or "")}
                    for sample in item.get("samples", []) or []
                ],
            )
    return summaries


def infer_modality_from_geo(item: dict) -> str:
    text = " ".join([str(item.get("title") or ""), str(item.get("summary") or ""), str(item.get("gdstype") or "")]).lower()
    if any(term in text for term in ("single-cell", "single cell", "scrna", "snrna")):
        return "single-cell RNA-seq"
    if any(term in text for term in ("rna sequencing", "rna-seq", "high throughput sequencing")):
        return "bulk RNA-seq"
    if "microarray" in text or "array" in text:
        return "microarray"
    return "unspecified omics"


def select_analysis_ready_hits(
    hits: list[dict[str, str]],
    summaries: dict[str, GeoSummary],
    *,
    max_datasets: int,
    accessions: list[str] | None = None,
) -> list[dict[str, str]]:
    requested = {accession.upper() for accession in accessions or []}
    ready: list[dict[str, str]] = []
    for hit in hits:
        accession = hit.get("accession", "")
        if not accession.startswith("GSE"):
            continue
        if requested and accession.upper() not in requested:
            continue
        summary = summaries.get(accession)
        if not summary:
            continue
        suppfile = summary.suppfile.lower()
        if not any(token in suppfile for token in ("txt", "tsv", "csv", "xlsx", "xls", "mtx")):
            continue
        if any(token in suppfile for token in ("fastq", "sra", "bam")):
            continue
        ready.append(hit)
    ready.sort(
        key=lambda row: (
            has_case_control_labels(summaries.get(row.get("accession", ""))),
            processed_matrix_priority(summaries.get(row.get("accession", ""))),
            int(float(row.get("relevance_score") or 0)),
        ),
        reverse=True,
    )
    return ready[:max_datasets]


def processed_matrix_priority(summary: GeoSummary | None) -> int:
    if not summary:
        return 0
    suppfile = re.sub(r"[^a-z0-9]+", " ", summary.suppfile.lower())
    score = 0
    if "mtx" in suppfile or "matrix" in suppfile:
        score += 40
    if any(token in suppfile for token in ("tsv", "txt", "csv")):
        score += 30
    if any(token in suppfile for token in ("xlsx", "xls")):
        score += 10
    if "filelist txt" in suppfile:
        score += 5
    return score


def has_case_control_labels(summary: GeoSummary | None) -> bool:
    if not summary:
        return False
    labels = [classify_sample_text(sample.get("title", "")) for sample in summary.samples]
    return labels.count("case") >= 2 and labels.count("control") >= 2


def analyze_geo_dataset(
    summary: GeoSummary,
    dataset_dir: Path,
    *,
    max_download_mb: int,
    force: bool,
) -> AnalysisResult:
    dataset_dir.mkdir(parents=True, exist_ok=True)
    (dataset_dir / "geo_summary.json").write_text(json.dumps(summary.__dict__, indent=2, ensure_ascii=False), encoding="utf-8")
    links = list_geo_supplementary_links(summary.ftplink)
    links = [link for link in links if is_supported_processed_file(link)]
    if not links:
        report = write_dataset_report(dataset_dir, summary, AnalysisResult(summary.accession, "skipped", "No supported processed supplementary matrix/table files found."))
        return AnalysisResult(summary.accession, "skipped", "No supported processed supplementary matrix/table files found.", report_path=str(report))

    downloaded = download_supplementary_files(links, dataset_dir / "downloads", max_download_mb=max_download_mb, force=force)
    downloaded = expand_and_download_filelist_links(
        downloaded,
        summary.ftplink,
        dataset_dir / "downloads",
        max_download_mb=max_download_mb,
        force=force,
    )
    if not downloaded:
        report = write_dataset_report(dataset_dir, summary, AnalysisResult(summary.accession, "skipped", "No files downloaded within size/type limits."))
        return AnalysisResult(summary.accession, "skipped", "No files downloaded within size/type limits.", report_path=str(report))

    matrix = None
    matrix_path = None
    parse_errors: list[str] = []
    try:
        mtx_matrix = build_pseudobulk_from_mtx_files(downloaded)
        if mtx_matrix is not None and not mtx_matrix.empty:
            matrix = mtx_matrix
            matrix_path = dataset_dir / "pseudobulk_from_mtx.tsv.gz"
            matrix.to_csv(matrix_path, sep="\t", compression="gzip")
    except Exception as exc:
        parse_errors.append(f"MTX pseudobulk: {type(exc).__name__}: {exc}")

    for path in downloaded:
        if matrix is not None:
            break
        try:
            matrix = read_expression_matrix(path)
            matrix_path = path
            if matrix is not None:
                break
        except Exception as exc:
            parse_errors.append(f"{path.name}: {type(exc).__name__}: {exc}")

    if matrix is None or matrix.empty:
        reason = "Downloaded files did not contain a recognizable gene-by-sample numeric matrix."
        if parse_errors:
            reason += " Parse notes: " + "; ".join(parse_errors[:3])
        result = AnalysisResult(summary.accession, "skipped", reason)
        report = write_dataset_report(dataset_dir, summary, result)
        result.report_path = str(report)
        return result

    sample_groups = infer_sample_groups(list(matrix.columns), summary.samples)
    comparison = f"{len(sample_groups['case'])} case vs {len(sample_groups['control'])} control samples"
    candidate_path = dataset_dir / "candidate_gene_check.tsv"
    candidate = candidate_gene_check(matrix, sample_groups)
    candidate.to_csv(candidate_path, sep="\t", index=False)

    de_path = ""
    if len(sample_groups["case"]) >= 2 and len(sample_groups["control"]) >= 2:
        de = differential_analysis(matrix, sample_groups)
        de_path_obj = dataset_dir / "de_results.tsv"
        de.to_csv(de_path_obj, sep="\t", index=False)
        de_path = str(de_path_obj)

    result = AnalysisResult(
        accession=summary.accession,
        status="completed",
        reason="Processed expression matrix parsed and analyzed.",
        matrix_file=str(matrix_path),
        n_genes=int(matrix.shape[0]),
        n_samples=int(matrix.shape[1]),
        comparison=comparison,
        candidate_gene_path=str(candidate_path),
        de_results_path=de_path,
    )
    report = write_dataset_report(dataset_dir, summary, result, candidate_preview=candidate)
    result.report_path = str(report)
    return result


def list_geo_supplementary_links(ftplink: str) -> list[str]:
    if not ftplink:
        return []
    base = ftplink.replace("ftp://ftp.ncbi.nlm.nih.gov", "https://ftp.ncbi.nlm.nih.gov").rstrip("/")
    suppl = base + "/suppl/"
    html_text = url_get(suppl, timeout=30)
    parser = LinkParser()
    parser.feed(html_text)
    links: list[str] = []
    for href in parser.links:
        if href in ("../", "/"):
            continue
        links.append(urllib.parse.urljoin(suppl, href))
    return links


def is_supported_processed_file(url: str) -> bool:
    lower = urllib.parse.unquote(url).lower()
    if any(lower.endswith(suffix) for suffix in SKIP_SUFFIXES):
        return False
    return any(lower.endswith(suffix) for suffix in SUPPORTED_TABLE_SUFFIXES)


def download_supplementary_files(
    links: list[str],
    output_dir: Path,
    *,
    max_download_mb: int,
    force: bool,
) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    downloaded: list[Path] = []
    budget_bytes = max_download_mb * 1024 * 1024
    used = 0
    for link in links:
        filename = Path(urllib.parse.unquote(urllib.parse.urlparse(link).path)).name
        target = output_dir / sanitize_filename(filename)
        size = remote_content_length(link)
        if target.exists() and not force:
            if size and target.stat().st_size != size:
                target.unlink()
            else:
                downloaded.append(target)
                used += target.stat().st_size
                continue
        if target.exists() and force:
            target.unlink()
        if size and used + size > budget_bytes:
            continue
        tmp_target = target.with_suffix(target.suffix + ".part")
        if tmp_target.exists():
            tmp_target.unlink()
        written = 0
        try:
            curl = shutil.which("curl") or shutil.which("curl.exe")
            if curl:
                curl_ok = download_with_curl(link, tmp_target, max_seconds=300)
                if not curl_ok:
                    continue
                written = tmp_target.stat().st_size
            else:
                request = urllib.request.Request(link, headers={"User-Agent": "MK-Hypoxia-MultiAgent/1.0"})
                with urllib.request.urlopen(request, timeout=120) as response, tmp_target.open("wb") as handle:
                    while True:
                        chunk = response.read(1024 * 1024)
                        if not chunk:
                            break
                        if used + written + len(chunk) > budget_bytes:
                            written = -1
                            break
                        handle.write(chunk)
                        written += len(chunk)
            if written < 0 or (size and written != size) or used + written > budget_bytes:
                if tmp_target.exists():
                    tmp_target.unlink()
                continue
            tmp_target.replace(target)
        except Exception:
            if tmp_target.exists():
                tmp_target.unlink()
            continue
        downloaded.append(target)
        used += target.stat().st_size
    return downloaded


def download_with_curl(url: str, target: Path, *, max_seconds: int) -> bool:
    curl = shutil.which("curl") or shutil.which("curl.exe")
    if not curl:
        return False
    result = subprocess.run(
        [
            curl,
            "-L",
            "--fail",
            "--silent",
            "--show-error",
            "--connect-timeout",
            "30",
            "--max-time",
            str(max_seconds),
            "--speed-limit",
            "1024",
            "--speed-time",
            "60",
            "-o",
            str(target),
            url,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=max_seconds + 30,
    )
    if result.returncode == 0 and target.exists() and target.stat().st_size > 0:
        return True
    if target.exists():
        target.unlink()
    return False


def expand_and_download_filelist_links(
    downloaded: list[Path],
    ftplink: str,
    output_dir: Path,
    *,
    max_download_mb: int,
    force: bool,
) -> list[Path]:
    filelists = [path for path in downloaded if path.name.lower().endswith("filelist.txt")]
    if not filelists or not ftplink:
        return downloaded

    base = ftplink.replace("ftp://ftp.ncbi.nlm.nih.gov", "https://ftp.ncbi.nlm.nih.gov").rstrip("/") + "/suppl/"
    expanded_links: list[str] = []
    archive_links: list[str] = []
    seen: set[str] = set()
    for filelist in filelists:
        for line in filelist.read_text(encoding="utf-8", errors="replace").splitlines():
            if not line or line.lower().startswith("type\t"):
                continue
            parts = line.split("\t")
            if len(parts) < 2:
                continue
            row_type = parts[0].strip().lower()
            name = parts[1].strip()
            if not name or name in seen:
                continue
            lower = name.lower()
            if row_type == "archive" and lower.endswith((".tar", ".tar.gz", ".tgz")):
                seen.add(name)
                archive_links.append(urllib.parse.urljoin(base, name))
                continue
            if "barcode" in lower:
                continue
            if not is_supported_processed_file(name):
                continue
            seen.add(name)
            expanded_links.append(geo_supplement_file_url(name, fallback_base=base))

    already_used_mb = sum(path.stat().st_size for path in downloaded if path.exists()) // (1024 * 1024)
    remaining_mb = max(1, max_download_mb - int(already_used_mb))
    expanded = download_supplementary_files(
        expanded_links,
        output_dir,
        max_download_mb=remaining_mb,
        force=force,
    )
    remaining_mb = max(1, remaining_mb - int(sum(path.stat().st_size for path in expanded if path.exists()) // (1024 * 1024)))
    archives = []
    if not expanded and archive_links:
        archives = download_supplementary_files(
            archive_links,
            output_dir,
            max_download_mb=remaining_mb,
            force=force,
        )
    archive_members = extract_supported_archive_files(archives, output_dir)
    combined = list(downloaded)
    existing = {path.resolve() for path in combined if path.exists()}
    for path in expanded + archives + archive_members:
        if path.exists() and path.resolve() not in existing:
            combined.append(path)
            existing.add(path.resolve())
    return combined


def geo_supplement_file_url(filename: str, *, fallback_base: str) -> str:
    match = re.search(r"(GSM\d+)", filename, flags=re.IGNORECASE)
    if not match:
        return urllib.parse.urljoin(fallback_base, filename)
    accession = match.group(1).upper()
    sample_group = accession[:-3] + "nnn"
    quoted = urllib.parse.quote(filename)
    return f"https://ftp.ncbi.nlm.nih.gov/geo/samples/{sample_group}/{accession}/suppl/{quoted}"


def extract_supported_archive_files(archives: list[Path], output_dir: Path) -> list[Path]:
    extracted: list[Path] = []
    for archive in archives:
        if not archive.exists() or not tarfile.is_tarfile(archive):
            continue
        try:
            with tarfile.open(archive, "r:*") as tar:
                for member in tar.getmembers():
                    if not member.isfile():
                        continue
                    basename = Path(member.name).name
                    lower = basename.lower()
                    if "barcode" in lower or not is_supported_processed_file(basename):
                        continue
                    source = tar.extractfile(member)
                    if source is None:
                        continue
                    target = output_dir / sanitize_filename(basename)
                    if target.exists():
                        extracted.append(target)
                        continue
                    with source, target.open("wb") as handle:
                        while True:
                            chunk = source.read(1024 * 1024)
                            if not chunk:
                                break
                            handle.write(chunk)
                    extracted.append(target)
        except tarfile.TarError:
            continue
    return extracted


def remote_content_length(url: str) -> int | None:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "MK-Hypoxia-MultiAgent/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            value = response.headers.get("Content-Length")
            return int(value) if value else None
    except Exception:
        return None


def read_expression_matrix(path: Path) -> pd.DataFrame | None:
    suffix = path.name.lower()
    if suffix.endswith((".mtx", ".mtx.gz")):
        return None
    if suffix.endswith((".xlsx", ".xls")):
        sheets = pd.read_excel(path, sheet_name=None)
        frames = list(sheets.values())
    else:
        opener = gzip.open if suffix.endswith(".gz") else open
        with opener(path, "rt", encoding="utf-8", errors="replace") as handle:
            sample = handle.read(4096)
        sep = "," if sample.count(",") > sample.count("\t") else "\t"
        frames = [pd.read_csv(path, sep=sep, compression="infer", low_memory=False)]

    best: pd.DataFrame | None = None
    best_score = -1
    for frame in frames:
        matrix = coerce_gene_by_sample_matrix(frame)
        if matrix is None:
            continue
        score = matrix.shape[0] * max(matrix.shape[1], 1)
        if score > best_score:
            best = matrix
            best_score = score
    return best


def build_pseudobulk_from_mtx_files(downloaded: list[Path]) -> pd.DataFrame | None:
    groups: dict[str, list[Path]] = {}
    for path in downloaded:
        match = re.search(r"(GSM\d+)", path.name, flags=re.IGNORECASE)
        if not match:
            continue
        groups.setdefault(match.group(1).upper(), []).append(path)

    columns: dict[str, pd.Series] = {}
    for accession, files in groups.items():
        feature_file = choose_file(files, ("features", "genes"), (".tsv", ".tsv.gz", ".txt", ".txt.gz"))
        matrix_file = choose_file(files, ("matrix",), (".mtx", ".mtx.gz"))
        if not feature_file or not matrix_file:
            continue
        genes = read_10x_features(feature_file)
        values = read_mtx_gene_sums(matrix_file, expected_rows=len(genes))
        if not genes or values.size == 0:
            continue
        n = min(len(genes), len(values))
        sample_name = sample_name_from_mtx_files(accession, files)
        columns[sample_name] = pd.Series(values[:n], index=genes[:n], dtype=float)

    if len(columns) < 2:
        return None

    matrix = pd.DataFrame(columns).fillna(0.0)
    matrix = matrix.groupby(matrix.index).sum()
    matrix = matrix.loc[matrix.sum(axis=1) > 0]
    if matrix.shape[0] < 50:
        return None
    return matrix


def choose_file(files: list[Path], name_tokens: tuple[str, ...], suffixes: tuple[str, ...]) -> Path | None:
    candidates = [
        path
        for path in files
        if any(token in path.name.lower() for token in name_tokens)
        and any(path.name.lower().endswith(suffix) for suffix in suffixes)
    ]
    return sorted(candidates, key=lambda path: len(path.name))[0] if candidates else None


def read_10x_features(path: Path) -> list[str]:
    opener = gzip.open if path.name.lower().endswith(".gz") else open
    genes: list[str] = []
    with opener(path, "rt", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 2 and parts[1]:
                genes.append(parts[1])
            elif parts and parts[0]:
                genes.append(parts[0])
    return genes


def read_mtx_gene_sums(path: Path, *, expected_rows: int) -> np.ndarray:
    opener = gzip.open if path.name.lower().endswith(".gz") else open
    values: np.ndarray | None = None
    with opener(path, "rt", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            if not line.strip() or line.startswith("%"):
                continue
            parts = line.split()
            if values is None:
                n_rows = int(parts[0]) if parts else expected_rows
                values = np.zeros(max(n_rows, expected_rows), dtype=float)
                continue
            if len(parts) < 3:
                continue
            gene_index = int(parts[0]) - 1
            if 0 <= gene_index < len(values):
                values[gene_index] += float(parts[2])
    return values if values is not None else np.array([], dtype=float)


def sample_name_from_mtx_files(accession: str, files: list[Path]) -> str:
    names = sorted(path.name for path in files)
    for name in names:
        cleaned = re.sub(r"_(features|genes|matrix)\.(tsv|txt|mtx)(\.gz)?$", "", name, flags=re.IGNORECASE)
        if cleaned != name:
            return cleaned
    return accession


def coerce_gene_by_sample_matrix(frame: pd.DataFrame) -> pd.DataFrame | None:
    if frame.empty or frame.shape[1] < 3:
        return None
    frame = frame.copy()
    gene_col = detect_gene_column(frame)
    if gene_col is None:
        return None
    genes = frame[gene_col].astype(str).str.strip()
    numeric = frame.drop(columns=[gene_col]).apply(pd.to_numeric, errors="coerce")
    numeric = numeric.dropna(axis=1, thresh=max(3, int(len(numeric) * 0.2)))
    if numeric.shape[1] < 2:
        return None
    numeric.index = genes
    numeric = numeric[~numeric.index.duplicated(keep="first")]
    numeric = numeric.loc[numeric.index.notna()]
    numeric = numeric.loc[numeric.index.astype(str).str.len() > 0]
    numeric = numeric.dropna(axis=0, how="all")
    if numeric.shape[0] < 50:
        return None
    return numeric


def detect_gene_column(frame: pd.DataFrame) -> str | None:
    candidates = {"gene", "genes", "gene_symbol", "symbol", "genesymbol", "geneid", "gene_id", "id", "feature", "features"}
    for col in frame.columns:
        normalized = re.sub(r"[^a-z0-9]", "", str(col).lower())
        if normalized in {re.sub(r"[^a-z0-9]", "", item) for item in candidates}:
            return col
    first = frame.columns[0]
    non_numeric = pd.to_numeric(frame[first], errors="coerce").isna().mean()
    return first if non_numeric > 0.8 else None


def infer_sample_groups(columns: list[str], samples: list[dict[str, str]]) -> dict[str, list[str]]:
    sample_text: dict[str, str] = {}
    for sample in samples:
        accession = sample.get("accession", "")
        title = sample.get("title", "")
        if accession:
            sample_text[accession.lower()] = f"{accession} {title}".lower()
    groups = {"case": [], "control": [], "unknown": []}
    for col in columns:
        text = str(col).lower()
        for accession, combined in sample_text.items():
            if accession in text:
                text = combined
                break
        label = classify_sample_text(text)
        groups[label].append(col)
    return groups


def classify_sample_text(text: str) -> str:
    lower = text.lower()
    case_terms = ("hyp", "pah", "ph", "suhx", "mct", "disease", "treat", "ko", "knockout")
    control_terms = ("control", "ctrl", "con", "healthy", "normoxia", "room air", " ra", "_ra", "sham", "wt c", "ctr")
    case_hit = any(term in lower for term in case_terms)
    control_hit = any(term in lower for term in control_terms)
    if case_hit and not control_hit:
        return "case"
    if control_hit and not case_hit:
        return "control"
    return "unknown"


def candidate_gene_check(matrix: pd.DataFrame, sample_groups: dict[str, list[str]]) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    upper_index = {str(gene).upper(): gene for gene in matrix.index}
    for gene in CANDIDATE_GENES:
        original = upper_index.get(gene.upper())
        if original is None:
            rows.append({"gene": gene, "present": False, "mean_case": "", "mean_control": "", "log2fc_case_vs_control": "", "note": "not found"})
            continue
        values = matrix.loc[original]
        case = values[sample_groups["case"]].astype(float) if sample_groups["case"] else pd.Series(dtype=float)
        control = values[sample_groups["control"]].astype(float) if sample_groups["control"] else pd.Series(dtype=float)
        if len(case) and len(control):
            log2fc = log2(mean_positive(case) + 1.0) - log2(mean_positive(control) + 1.0)
            note = "case/control inferred from sample titles"
        else:
            log2fc = ""
            note = "gene found; insufficient group labels for log2FC"
        rows.append(
            {
                "gene": gene,
                "present": True,
                "mean_case": round(mean_positive(case), 4) if len(case) else "",
                "mean_control": round(mean_positive(control), 4) if len(control) else "",
                "log2fc_case_vs_control": round(log2fc, 4) if isinstance(log2fc, float) else "",
                "note": note,
            }
        )
    return pd.DataFrame(rows)


def differential_analysis(matrix: pd.DataFrame, sample_groups: dict[str, list[str]]) -> pd.DataFrame:
    case_cols = sample_groups["case"]
    control_cols = sample_groups["control"]
    rows: list[dict[str, object]] = []
    for gene, values in matrix.iterrows():
        case = pd.to_numeric(values[case_cols], errors="coerce").dropna().astype(float)
        control = pd.to_numeric(values[control_cols], errors="coerce").dropna().astype(float)
        if len(case) < 2 or len(control) < 2:
            continue
        mean_case = mean_positive(case)
        mean_control = mean_positive(control)
        log2fc = log2(mean_case + 1.0) - log2(mean_control + 1.0)
        p_value = approximate_welch_pvalue(case, control)
        rows.append(
            {
                "gene": gene,
                "mean_case": mean_case,
                "mean_control": mean_control,
                "log2fc_case_vs_control": log2fc,
                "p_value_approx": p_value,
            }
        )
    result = pd.DataFrame(rows)
    if result.empty:
        return result
    result["fdr_approx"] = benjamini_hochberg(result["p_value_approx"].to_numpy())
    result = result.sort_values(["p_value_approx", "log2fc_case_vs_control"], ascending=[True, False])
    return result.head(5000)


def approximate_welch_pvalue(case: pd.Series, control: pd.Series) -> float:
    c1 = case.to_numpy(dtype=float)
    c0 = control.to_numpy(dtype=float)
    var = np.var(c1, ddof=1) / len(c1) + np.var(c0, ddof=1) / len(c0)
    if not np.isfinite(var) or var <= 0:
        return 1.0
    t_stat = (np.mean(c1) - np.mean(c0)) / math.sqrt(var)
    return float(math.erfc(abs(t_stat) / math.sqrt(2)))


def benjamini_hochberg(p_values: np.ndarray) -> np.ndarray:
    p_values = np.asarray(p_values, dtype=float)
    order = np.argsort(p_values)
    ranked = np.empty_like(p_values)
    n = len(p_values)
    prev = 1.0
    for i in range(n - 1, -1, -1):
        idx = order[i]
        value = min(prev, p_values[idx] * n / (i + 1))
        ranked[idx] = value
        prev = value
    return ranked


def mean_positive(values: pd.Series) -> float:
    if len(values) == 0:
        return 0.0
    return float(np.nanmean(pd.to_numeric(values, errors="coerce").clip(lower=0)))


def log2(value: float) -> float:
    return math.log(value, 2)


def write_dataset_report(
    dataset_dir: Path,
    summary: GeoSummary,
    result: AnalysisResult,
    *,
    candidate_preview: pd.DataFrame | None = None,
) -> Path:
    path = dataset_dir / "analysis_report.md"
    lines = [
        f"# Public Dataset Analysis: {summary.accession}",
        "",
        f"- Title: {summary.title}",
        f"- Organism: {summary.organism or 'not specified'}",
        f"- Modality: {summary.modality}",
        f"- Status: {result.status}",
        f"- Reason: {result.reason}",
        f"- Matrix file: {result.matrix_file or 'none'}",
        f"- Genes x samples: {result.n_genes} x {result.n_samples}",
        f"- Comparison: {result.comparison or 'not available'}",
    ]
    if result.candidate_gene_path:
        lines.append(f"- Candidate gene check: {result.candidate_gene_path}")
    if result.de_results_path:
        lines.append(f"- Differential analysis: {result.de_results_path}")
    if candidate_preview is not None and not candidate_preview.empty:
        lines.extend(
            [
                "",
                "## Candidate Gene Preview",
                "| Gene | Present | log2FC case vs control | Note |",
                "|---|---|---:|---|",
            ]
        )
        for _, row in candidate_preview.head(20).iterrows():
            lines.append(
                f"| {md_escape(row['gene'])} | {row['present']} | {row['log2fc_case_vs_control']} | {md_escape(row['note'])} |"
            )
    path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    return path


def format_analysis_context(results: list[AnalysisResult], manifest: dict) -> str:
    lines = [
        "# Public Dataset Analysis Context",
        "",
        "Purpose: analyze processed public dataset matrices when available. This module does not process FASTQ/SRA files.",
        f"- Analysis enabled: {manifest.get('enabled')}",
        f"- Results: {len(results)}",
    ]
    issues = manifest.get("access_issues") or []
    if issues:
        lines.append("- Access or analysis issues:")
        for issue in issues:
            lines.append(f"  - {issue}")
    lines.extend(
        [
            "",
            "## Dataset Analysis Summary",
            "| Accession | Status | Matrix | Genes | Samples | Comparison | Key outputs | Reason |",
            "|---|---|---|---:|---:|---|---|---|",
        ]
    )
    for result in results:
        outputs = []
        if result.candidate_gene_path:
            outputs.append(f"[candidate genes]({result.candidate_gene_path})")
        if result.de_results_path:
            outputs.append(f"[DE results]({result.de_results_path})")
        if result.report_path:
            outputs.append(f"[report]({result.report_path})")
        lines.append(
            "| "
            + " | ".join(
                [
                    md_escape(result.accession),
                    md_escape(result.status),
                    md_escape(Path(result.matrix_file).name if result.matrix_file else "none"),
                    str(result.n_genes),
                    str(result.n_samples),
                    md_escape(result.comparison or "not available"),
                    ", ".join(outputs) or "none",
                    md_escape(shorten(result.reason, 120)),
                ]
            )
            + " |"
        )
    if not results:
        lines.append("| none | not run | none | 0 | 0 | not available | none | analysis disabled or no analysis-ready hits |")
    lines.extend(
        [
            "",
            "## Interpretation Rules",
            "- Completed analyses may be treated as public-data evidence at the expression-matrix level.",
            "- Skipped datasets remain metadata-only validation opportunities.",
            "- Approximate differential analysis uses inferred sample labels and lightweight statistics; validate important findings manually.",
            "- Do not treat absent candidate genes as biological absence when identifiers may use Ensembl IDs or probe IDs.",
        ]
    )
    return "\n".join(lines).strip() + "\n"


def sanitize_filename(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("._") or "downloaded_file"
