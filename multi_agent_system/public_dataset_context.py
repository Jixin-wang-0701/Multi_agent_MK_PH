from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
import csv
import hashlib
import json
import re
import urllib.error
import urllib.parse
import urllib.request


NCBI_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
BIOSTUDIES_BASE = "https://www.ebi.ac.uk/biostudies/api/v1"

DEFAULT_PUBLIC_DATASET_TASKS = [
    "pulmonary hypertension hypoxia lung transcriptomics",
    "pulmonary hypertension vascular remodeling lung single cell",
    "megakaryocyte platelet lung pulmonary hypertension",
    "hypoxia pulmonary artery endothelial smooth muscle RNA-seq",
    "pulmonary hypertension lung proteomics metabolomics",
    "vascular remodeling extracellular matrix lung hypoxia dataset",
]

ORGANISM_TERMS = ("human", "mouse", "mus musculus", "homo sapiens", "rat")
TISSUE_TERMS = ("lung", "pulmonary", "pulmonary artery", "vascular", "endothelial", "smooth muscle")
DISEASE_TERMS = ("pulmonary hypertension", "hypoxia", "vascular remodeling", "pulmonary arterial hypertension")
CELL_TERMS = ("megakaryocyte", "platelet", "endothelial", "smooth muscle", "fibroblast", "macrophage")
MODALITY_TERMS = (
    "single cell",
    "scrna",
    "snrna",
    "spatial",
    "rna-seq",
    "transcriptomic",
    "proteomic",
    "metabolomic",
    "microarray",
)


@dataclass(frozen=True)
class DatasetSearchTask:
    query: str
    source_hint: str = "public repositories"
    priority: str = "medium"


@dataclass
class PublicDatasetHit:
    source: str
    accession: str
    title: str
    summary: str
    organism: str = ""
    modality: str = ""
    sample_count: str = ""
    query: str = ""
    relevance_score: int = 0
    relevance_label: str = "low"
    source_url: str = ""
    retrieved_at: str = ""


def build_public_dataset_context(
    root: Path,
    output_dir: Path,
    *,
    pi_brief: str = "",
    enabled: bool = True,
    max_results: int = 8,
) -> Path:
    public_dir = output_dir / "public_datasets"
    cache_dir = public_dir / "cache"
    public_dir.mkdir(parents=True, exist_ok=True)
    cache_dir.mkdir(parents=True, exist_ok=True)

    tasks = build_search_tasks(pi_brief)
    retrieved_at = datetime.now().isoformat(timespec="seconds")
    hits: list[PublicDatasetHit] = []
    access_issues: list[str] = []

    if enabled:
        for task in tasks:
            try:
                hits.extend(search_geo(task, cache_dir, max_results=max_results, retrieved_at=retrieved_at))
            except Exception as exc:
                access_issues.append(f"GEO search failed for query '{task.query}': {type(exc).__name__}: {exc}")
            try:
                hits.extend(search_biostudies(task, cache_dir, max_results=max(3, max_results // 2), retrieved_at=retrieved_at))
            except Exception as exc:
                access_issues.append(
                    f"EBI BioStudies/ArrayExpress search failed for query '{task.query}': {type(exc).__name__}: {exc}"
                )
    else:
        access_issues.append("Public dataset search disabled by runtime option.")

    hits = rank_and_dedupe_hits(hits)
    csv_path = public_dir / "public_dataset_hits.csv"
    write_hits_csv(csv_path, hits)

    manifest = {
        "generated_at": retrieved_at,
        "enabled": enabled,
        "task_count": len(tasks),
        "tasks": [asdict(task) for task in tasks],
        "hit_count": len(hits),
        "access_issues": access_issues,
        "outputs": {
            "public_dataset_hits": str(csv_path),
        },
    }
    manifest_path = public_dir / "public_dataset_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    context_path = output_dir / "public_dataset_context.md"
    context_path.write_text(format_public_dataset_context(tasks, hits, access_issues, csv_path, manifest_path), encoding="utf-8")
    return context_path


def build_search_tasks(pi_brief: str) -> list[DatasetSearchTask]:
    queries: list[str] = []
    public_block = extract_public_dataset_block(pi_brief)
    for line in public_block:
        cleaned = clean_query_line(line)
        if cleaned:
            queries.append(cleaned)

    if not queries:
        queries = list(DEFAULT_PUBLIC_DATASET_TASKS)

    deduped: list[str] = []
    seen: set[str] = set()
    for query in queries:
        key = re.sub(r"\s+", " ", query.lower()).strip()
        if key and key not in seen:
            deduped.append(query)
            seen.add(key)
    return [DatasetSearchTask(query=query) for query in deduped[:8]]


def extract_public_dataset_block(pi_brief: str) -> list[str]:
    lines = pi_brief.splitlines()
    selected: list[str] = []
    capture = False
    for line in lines:
        lower = line.lower()
        if any(
            marker in lower
            for marker in (
                "public dataset search",
                "public data search",
                "dataset search",
                "external dataset",
                "public repositories",
            )
        ):
            capture = True
            selected.append(line)
            continue
        if capture and re.match(r"^\s*(#{1,4}\s+|[A-Z][A-Za-z /-]+:\s*$)", line) and selected:
            break
        if capture:
            selected.append(line)
        if capture and len(selected) >= 14:
            break
    return selected


def clean_query_line(line: str) -> str:
    text = re.sub(r"^[\s#>*-]+", "", line).strip()
    text = re.sub(r"^\d+[\.)]\s*", "", text)
    if not text or ":" in text[:35] and "search" in text.lower():
        return ""
    text = text.replace("`", "").replace('"', "")
    text = re.sub(r"\([^)]*\)", "", text)
    text = re.sub(r"\s+", " ", text).strip(" ;,.")
    if len(text.split()) < 3:
        return ""
    return text[:180]


def search_geo(
    task: DatasetSearchTask,
    cache_dir: Path,
    *,
    max_results: int,
    retrieved_at: str,
) -> list[PublicDatasetHit]:
    term = task.query
    search_url = (
        f"{NCBI_BASE}/esearch.fcgi?db=gds&retmode=json&sort=relevance"
        f"&retmax={max_results}&term={urllib.parse.quote(term)}"
    )
    search_data = json.loads(cached_url_get(search_url, cache_dir, "geo_search", term))
    ids = search_data.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []
    summary_url = (
        f"{NCBI_BASE}/esummary.fcgi?db=gds&retmode=json&id="
        + ",".join(urllib.parse.quote(str(item)) for item in ids)
    )
    summary_data = json.loads(cached_url_get(summary_url, cache_dir, "geo_summary", ",".join(ids)))
    result = summary_data.get("result", {})
    hits: list[PublicDatasetHit] = []
    for uid in result.get("uids", []):
        item = result.get(uid, {})
        accession = str(item.get("accession") or item.get("gse") or item.get("gds") or uid)
        if not accession.startswith(("GSE", "GDS")):
            continue
        title = str(item.get("title") or item.get("summary") or accession)
        summary = str(item.get("summary") or item.get("description") or "")
        organism = first_nonempty(item.get("taxon"), item.get("organism"), item.get("sampletaxa"))
        modality = infer_modality(" ".join([title, summary, str(item.get("gdstype", ""))]))
        sample_count = first_nonempty(item.get("n_samples"), item.get("samples"), item.get("samplecount"))
        url_acc = accession if accession.startswith(("GSE", "GDS", "GPL", "GSM")) else uid
        hit = PublicDatasetHit(
            source="NCBI GEO/GDS",
            accession=accession,
            title=title,
            summary=summary,
            organism=str(organism or ""),
            modality=modality,
            sample_count=str(sample_count or ""),
            query=term,
            source_url=f"https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={urllib.parse.quote(url_acc)}",
            retrieved_at=retrieved_at,
        )
        score_hit(hit)
        hits.append(hit)
    return hits


def search_biostudies(
    task: DatasetSearchTask,
    cache_dir: Path,
    *,
    max_results: int,
    retrieved_at: str,
) -> list[PublicDatasetHit]:
    url = (
        f"{BIOSTUDIES_BASE}/search?query={urllib.parse.quote(task.query)}"
        f"&pageSize={max_results}"
    )
    data = json.loads(cached_url_get(url, cache_dir, "biostudies_search", task.query))
    raw_hits = data.get("hits") or data.get("entries") or []
    hits: list[PublicDatasetHit] = []
    for item in raw_hits:
        accession = str(item.get("accession") or item.get("id") or "")
        if not accession:
            continue
        if not accession.startswith(("E-", "S-BSST", "S-BIAD")):
            continue
        title = str(item.get("title") or item.get("name") or accession)
        summary = str(item.get("description") or item.get("summary") or "")
        organism = extract_attribute(item, ("organism", "Organism", "species"))
        modality = infer_modality(" ".join([title, summary, str(item)]))
        hit = PublicDatasetHit(
            source="EBI BioStudies/ArrayExpress",
            accession=accession,
            title=title,
            summary=summary,
            organism=organism,
            modality=modality,
            query=task.query,
            source_url=f"https://www.ebi.ac.uk/biostudies/{urllib.parse.quote(accession)}",
            retrieved_at=retrieved_at,
        )
        score_hit(hit)
        hits.append(hit)
    return hits


def cached_url_get(url: str, cache_dir: Path, prefix: str, key: str) -> str:
    digest = hashlib.sha1(f"{url}\n{key}".encode("utf-8")).hexdigest()[:16]
    path = cache_dir / f"{prefix}_{digest}.json"
    if path.exists():
        return path.read_text(encoding="utf-8")
    text = url_get(url)
    path.write_text(text, encoding="utf-8")
    return text


def url_get(url: str, timeout: int = 25) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "MK-Hypoxia-MultiAgent/1.0 (public dataset discovery)",
            "Accept": "application/json,text/plain,*/*",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"HTTP {exc.code} for {url}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"URL error for {url}: {exc.reason}") from exc


def rank_and_dedupe_hits(hits: list[PublicDatasetHit]) -> list[PublicDatasetHit]:
    best: dict[str, PublicDatasetHit] = {}
    for hit in hits:
        if hit.relevance_score < 8:
            continue
        key = (hit.source.lower(), hit.accession.lower())
        if key not in best or hit.relevance_score > best[key].relevance_score:
            best[key] = hit
    return sorted(best.values(), key=lambda item: (item.relevance_score, item.accession), reverse=True)


def score_hit(hit: PublicDatasetHit) -> None:
    text = " ".join([hit.title, hit.summary, hit.organism, hit.modality]).lower()
    score = 0
    score += 3 * count_term_hits(text, DISEASE_TERMS)
    score += 2 * count_term_hits(text, TISSUE_TERMS)
    score += 2 * count_term_hits(text, CELL_TERMS)
    score += 2 * count_term_hits(text, MODALITY_TERMS)
    score += count_term_hits(text, ORGANISM_TERMS)
    hit.relevance_score = score
    if score >= 14:
        hit.relevance_label = "high"
    elif score >= 8:
        hit.relevance_label = "medium"
    else:
        hit.relevance_label = "low"


def count_term_hits(text: str, terms: tuple[str, ...]) -> int:
    return sum(1 for term in terms if term in text)


def infer_modality(text: str) -> str:
    lower = text.lower()
    checks = [
        ("spatial transcriptomics", ("spatial",)),
        ("single-cell RNA-seq", ("single cell", "single-cell", "scrna", "snrna")),
        ("bulk RNA-seq", ("rna-seq", "transcriptome", "transcriptomic")),
        ("microarray", ("microarray", "array")),
        ("proteomics", ("proteomic", "proteomics")),
        ("metabolomics", ("metabolomic", "metabolomics")),
    ]
    for label, terms in checks:
        if any(term in lower for term in terms):
            return label
    return "unspecified omics"


def first_nonempty(*values: object) -> object:
    for value in values:
        if value not in (None, "", [], {}):
            return value
    return ""


def extract_attribute(item: dict, names: tuple[str, ...]) -> str:
    for name in names:
        value = item.get(name)
        if isinstance(value, str) and value:
            return value
    for attr in item.get("attributes", []) or []:
        key = str(attr.get("name") or attr.get("type") or "")
        if key in names:
            value = attr.get("value") or attr.get("val")
            if value:
                return str(value)
    return ""


def write_hits_csv(path: Path, hits: list[PublicDatasetHit]) -> None:
    fields = [
        "source",
        "accession",
        "title",
        "summary",
        "organism",
        "modality",
        "sample_count",
        "query",
        "relevance_score",
        "relevance_label",
        "source_url",
        "retrieved_at",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for hit in hits:
            writer.writerow({field: getattr(hit, field) for field in fields})


def format_public_dataset_context(
    tasks: list[DatasetSearchTask],
    hits: list[PublicDatasetHit],
    access_issues: list[str],
    csv_path: Path,
    manifest_path: Path,
) -> str:
    lines = [
        "# Public Dataset Discovery Context",
        "",
        "Purpose: identify public datasets that could validate or extend MK-hypoxia-vascular remodeling hypotheses.",
        "This context is generated by programmatic repository queries. Agents must not claim an external dataset was inspected beyond the metadata shown here unless downstream code downloads and analyzes it.",
        "",
        "## Search Tasks",
    ]
    for index, task in enumerate(tasks, start=1):
        lines.append(f"{index}. {task.query} ({task.priority}; {task.source_hint})")

    lines.extend(
        [
            "",
            "## Access Status",
            f"- Hits retrieved: {len(hits)}",
            f"- CSV: {csv_path}",
            f"- Manifest: {manifest_path}",
        ]
    )
    if access_issues:
        lines.append("- Access issues:")
        for issue in access_issues:
            lines.append(f"  - {issue}")
    else:
        lines.append("- Access issues: none recorded")

    lines.extend(
        [
            "",
            "## Top Public Dataset Hits",
            "| Rank | Source | Accession | Relevance | Modality | Organism | Title | Why it may help |",
            "|---:|---|---|---|---|---|---|---|",
        ]
    )
    for index, hit in enumerate(hits[:20], start=1):
        lines.append(
            "| "
            + " | ".join(
                [
                    str(index),
                    md_escape(hit.source),
                    f"[{md_escape(hit.accession)}]({hit.source_url})",
                    f"{hit.relevance_label} ({hit.relevance_score})",
                    md_escape(hit.modality),
                    md_escape(hit.organism or "not specified"),
                    md_escape(shorten(hit.title, 120)),
                    md_escape(dataset_help_text(hit)),
                ]
            )
            + " |"
        )

    if not hits:
        lines.extend(
            [
                "",
                "No public dataset metadata was retrieved. Downstream agents should treat public dataset support as unavailable, not negative.",
            ]
        )

    lines.extend(
        [
            "",
            "## How Downstream Agents Should Use This",
            "- Treat these hits as candidate validation datasets, not direct mechanistic evidence.",
            "- Prefer hypotheses that can be tested against high- or medium-relevance datasets.",
            "- Clearly separate local user data, retrieved public dataset metadata, PubMed/KEGG context, and biological inference.",
            "- If a dataset lacks MK/platelet annotations, it may still support recipient-cell or tissue-level validation.",
            "- If no suitable dataset is found, state the gap and propose targeted experimental validation.",
        ]
    )
    return "\n".join(lines).strip() + "\n"


def dataset_help_text(hit: PublicDatasetHit) -> str:
    text = " ".join([hit.title, hit.summary]).lower()
    reasons: list[str] = []
    if any(term in text for term in ("pulmonary hypertension", "hypoxia", "pah")):
        reasons.append("disease/hypoxia context")
    if any(term in text for term in ("lung", "pulmonary", "vascular")):
        reasons.append("lung/vascular tissue context")
    if any(term in text for term in ("megakaryocyte", "platelet")):
        reasons.append("MK/platelet relevance")
    if any(term in text for term in ("endothelial", "smooth muscle", "fibroblast")):
        reasons.append("recipient-cell validation")
    if not reasons:
        reasons.append("broad metadata match")
    return "; ".join(reasons)


def md_escape(text: object) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def shorten(text: str, limit: int) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."
