from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import datetime
import json
import math
import os
from pathlib import Path
import re
import subprocess
import zipfile
from xml.etree import ElementTree as ET

from .r_support import WANTED_R_PACKAGES, select_rscript


PRIORITY_GENES = [
    "Pdgfb",
    "Tgfb1",
    "F3",
    "Thbs1",
    "Glo1",
    "Rab27a",
    "Tsg101",
    "Cd44",
    "Lox",
    "Loxl1",
    "Loxl2",
    "Mki67",
    "Amd1",
    "Amd2",
    "Pnp",
    "Nt5c2",
    "Nt5e",
]

PRIORITY_METABOLITES = {
    "methionine": ["methionine"],
    "inosine": ["inosine"],
    "adenosine": ["adenosine"],
    "spermidine": ["spermidine"],
    "spermine": ["spermine"],
    "S-adenosylmethionine": ["s-adenosylmethionine", "sam", "same"],
    "retinoic acid": ["retinoic acid"],
    "methylglyoxal / pyruvaldehyde": ["methylglyoxal", "pyruvaldehyde"],
}


@dataclass(frozen=True)
class EvidencePackage:
    path: Path
    manifest_path: Path
    text: str


def build_evidence_package(root: Path, output_dir: Path) -> EvidencePackage:
    """Build a local evidence package before hypothesis generation."""

    evidence_dir = output_dir / "evidence_package"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    generated = datetime.now().isoformat(timespec="seconds")

    seurat_csv = evidence_dir / "priority_gene_seurat_expression.csv"
    seurat_status = _run_seurat_gene_query(
        root / "seurat_merged.rds",
        root / "multi_agent_system" / "r_scripts" / "score_metabolic_genes.R",
        evidence_dir / "priority_gene_list.csv",
        seurat_csv,
    )

    public_de_csv = evidence_dir / "priority_gene_public_de.csv"
    public_de_status = _extract_public_de(
        output_dir / "public_dataset_analysis" / "GSE289322" / "de_results.tsv",
        public_de_csv,
    )

    metabolite_csv = evidence_dir / "priority_metabolite_crosscheck.csv"
    metabolite_status = _extract_metabolites(root, metabolite_csv)

    text = _render_evidence_markdown(
        generated,
        seurat_csv,
        seurat_status,
        public_de_csv,
        public_de_status,
        metabolite_csv,
        metabolite_status,
    )
    path = output_dir / "evidence_package.md"
    path.write_text(text, encoding="utf-8")

    manifest = {
        "generated": generated,
        "priority_genes": PRIORITY_GENES,
        "priority_metabolites": list(PRIORITY_METABOLITES),
        "evidence_package": str(path),
        "seurat_gene_expression": str(seurat_csv),
        "public_de": str(public_de_csv),
        "metabolite_crosscheck": str(metabolite_csv),
        "statuses": {
            "seurat": seurat_status,
            "public_de": public_de_status,
            "metabolites": metabolite_status,
        },
    }
    manifest_path = evidence_dir / "evidence_package_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return EvidencePackage(path=path, manifest_path=manifest_path, text=text)


def _run_seurat_gene_query(
    rds_path: Path,
    script_path: Path,
    gene_csv: Path,
    output_csv: Path,
) -> str:
    with gene_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["gene_symbol"])
        writer.writeheader()
        for gene in PRIORITY_GENES:
            writer.writerow({"gene_symbol": gene})

    if not rds_path.exists():
        return f"skipped: missing RDS file {rds_path}"
    if not script_path.exists():
        return f"skipped: missing R script {script_path}"
    rscript = select_rscript()
    if not rscript:
        return "skipped: no usable Rscript found"

    try:
        result = subprocess.run(
            [str(rscript), str(script_path), str(rds_path), str(gene_csv), str(output_csv)],
            text=True,
            capture_output=True,
            timeout=900,
            check=False,
            env={**os.environ, "MULTI_AGENT_R_PACKAGES": ",".join(WANTED_R_PACKAGES)},
        )
    except Exception as exc:  # noqa: BLE001 - local runtime issue should be recorded verbatim.
        return f"failed: {exc}"

    if result.returncode != 0:
        stderr = result.stderr.strip() or "[empty stderr]"
        stdout = result.stdout.strip() or "[empty stdout]"
        message = f"failed: R return code {result.returncode}; stdout={stdout[:500]}; stderr={stderr[:500]}"
        if output_csv.exists():
            return message + "; using existing output table from a previous successful run"
        _write_dict_rows(output_csv, _empty_seurat_rows(), _seurat_fields())
        return message
    return "completed"


def _seurat_fields() -> list[str]:
    return [
        "gene_symbol",
        "matched_feature",
        "status",
        "assay",
        "mk_pct_expr",
        "other_pct_expr",
        "mk_mean_expr",
        "other_mean_expr",
        "mk_enrichment_log2",
        "ph_mk_mean_expr",
        "control_mk_mean_expr",
        "ph_vs_control_mk_log2",
        "ph_mk_pct_expr",
        "control_mk_pct_expr",
        "ph_vs_control_mk_p_value",
        "mk_vs_other_p_value",
    ]


def _empty_seurat_rows() -> list[dict[str, str]]:
    return [
        {
            "gene_symbol": gene,
            "matched_feature": "",
            "status": "not_queried",
            "assay": "",
            "mk_pct_expr": "",
            "other_pct_expr": "",
            "mk_mean_expr": "",
            "other_mean_expr": "",
            "mk_enrichment_log2": "",
            "ph_mk_mean_expr": "",
            "control_mk_mean_expr": "",
            "ph_vs_control_mk_log2": "",
            "ph_mk_pct_expr": "",
            "control_mk_pct_expr": "",
            "ph_vs_control_mk_p_value": "",
            "mk_vs_other_p_value": "",
        }
        for gene in PRIORITY_GENES
    ]


def _extract_public_de(de_path: Path, output_csv: Path) -> str:
    rows: list[dict[str, str]] = []
    if not de_path.exists():
        _write_dict_rows(output_csv, rows, ["gene", "matched", "note"])
        return f"skipped: missing DE file {de_path}"

    wanted = {gene.upper(): gene for gene in PRIORITY_GENES}
    with de_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        fieldnames = reader.fieldnames or []
        gene_field = "gene" if "gene" in fieldnames else fieldnames[0] if fieldnames else ""
        for row in reader:
            gene_id = (row.get(gene_field) or "").strip()
            if gene_id.upper() in wanted:
                out = {"query_gene": wanted[gene_id.upper()], "matched_identifier": gene_id}
                out.update({key: row.get(key, "") for key in fieldnames if key != gene_field})
                out["note"] = "matched by exact identifier"
                rows.append(out)

    found = {row["query_gene"].upper() for row in rows}
    for gene in PRIORITY_GENES:
        if gene.upper() not in found:
            rows.append(
                {
                    "query_gene": gene,
                    "matched_identifier": "",
                    "mean_case": "",
                    "mean_control": "",
                    "log2fc_case_vs_control": "",
                    "p_value_approx": "",
                    "fdr_approx": "",
                    "note": "not found by gene symbol; DE table appears to use Ensembl-like identifiers",
                }
            )

    fields = [
        "query_gene",
        "matched_identifier",
        "mean_case",
        "mean_control",
        "log2fc_case_vs_control",
        "p_value_approx",
        "fdr_approx",
        "note",
    ]
    _write_dict_rows(output_csv, rows, fields)
    return "completed with identifier-limited matching"


def _extract_metabolites(root: Path, output_csv: Path) -> str:
    rows: list[dict[str, str]] = []
    files = [
        root / "sFig6A Raw data.xlsx",
        root / "Figure6D+F raw data.xlsx",
    ]
    for path in files:
        if not path.exists():
            rows.append({"source_file": path.name, "sheet": "", "metabolite": "", "status": "missing file"})
            continue
        try:
            workbook = _read_xlsx_workbook(path)
        except Exception as exc:  # noqa: BLE001 - xlsx files may vary; keep report readable.
            rows.append({"source_file": path.name, "sheet": "", "metabolite": "", "status": f"read failed: {exc}"})
            continue

        for sheet_name, sheet_rows in workbook.items():
            if not sheet_rows:
                continue
            header = [str(value or "").strip() for value in sheet_rows[0]]
            for row in sheet_rows[1:]:
                if not row:
                    continue
                observed_name = str(row[0] or "").strip()
                if not observed_name:
                    continue
                canonical = _match_metabolite(observed_name)
                if not canonical:
                    continue
                rows.append(_summarize_metabolite_row(path.name, sheet_name, header, row, canonical, observed_name))

    found = {(row.get("source_file", ""), row.get("metabolite", "")) for row in rows}
    for path in files:
        for metabolite in PRIORITY_METABOLITES:
            if (path.name, metabolite) not in found:
                rows.append(
                    {
                        "source_file": path.name,
                        "sheet": "",
                        "metabolite": metabolite,
                        "matched_name": "",
                        "status": "not found",
                    }
                )

    fields = [
        "source_file",
        "sheet",
        "metabolite",
        "matched_name",
        "status",
        "control_mean",
        "case_mean",
        "log2fc_case_vs_control",
        "p_value",
        "fdr",
        "note",
    ]
    _write_dict_rows(output_csv, rows, fields)
    return "completed"


def _read_xlsx_workbook(path: Path) -> dict[str, list[list[object]]]:
    with zipfile.ZipFile(path) as archive:
        shared_strings = _read_shared_strings(archive)
        workbook_root = ET.fromstring(archive.read("xl/workbook.xml"))
        rels_root = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))

        rels = {}
        for rel in rels_root:
            rel_id = rel.attrib.get("Id")
            target = rel.attrib.get("Target", "")
            if rel_id and target:
                target = target.lstrip("/")
                rels[rel_id] = target if target.startswith("xl/") else "xl/" + target

        namespace = {
            "main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
            "rel": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
        }
        sheets: dict[str, list[list[object]]] = {}
        for sheet in workbook_root.findall(".//main:sheet", namespace):
            name = sheet.attrib.get("name", "Sheet")
            rel_id = sheet.attrib.get(f"{{{namespace['rel']}}}id")
            target = rels.get(rel_id or "")
            if not target or target not in archive.namelist():
                continue
            sheets[name] = _read_xlsx_sheet(archive, target, shared_strings)
        return sheets


def _read_shared_strings(archive: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in archive.namelist():
        return []
    root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
    namespace = {"main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    strings: list[str] = []
    for item in root.findall(".//main:si", namespace):
        parts = [node.text or "" for node in item.findall(".//main:t", namespace)]
        strings.append("".join(parts))
    return strings


def _read_xlsx_sheet(archive: zipfile.ZipFile, target: str, shared_strings: list[str]) -> list[list[object]]:
    root = ET.fromstring(archive.read(target))
    namespace = {"main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    rows: list[list[object]] = []
    for row in root.findall(".//main:sheetData/main:row", namespace):
        values: dict[int, object] = {}
        for cell in row.findall("main:c", namespace):
            ref = cell.attrib.get("r", "")
            col = _excel_col_index(ref)
            values[col] = _cell_value(cell, namespace, shared_strings)
        if values:
            max_col = max(values)
            rows.append([values.get(index, "") for index in range(max_col + 1)])
    return rows


def _excel_col_index(ref: str) -> int:
    letters = re.sub(r"[^A-Z]", "", ref.upper())
    index = 0
    for letter in letters:
        index = index * 26 + (ord(letter) - ord("A") + 1)
    return max(0, index - 1)


def _cell_value(cell: ET.Element, namespace: dict[str, str], shared_strings: list[str]) -> object:
    cell_type = cell.attrib.get("t", "")
    value_node = cell.find("main:v", namespace)
    if cell_type == "inlineStr":
        text_parts = [node.text or "" for node in cell.findall(".//main:t", namespace)]
        return "".join(text_parts)
    if value_node is None or value_node.text is None:
        return ""
    raw = value_node.text
    if cell_type == "s":
        try:
            return shared_strings[int(raw)]
        except Exception:
            return raw
    try:
        number = float(raw)
    except ValueError:
        return raw
    if number.is_integer():
        return int(number)
    return number


def _match_metabolite(value: str) -> str:
    normalized = _normalize_name(value)
    for canonical, aliases in PRIORITY_METABOLITES.items():
        for alias in aliases:
            if _normalize_name(alias) == normalized:
                return canonical
    return ""


def _normalize_name(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def _summarize_metabolite_row(
    source_file: str,
    sheet: str,
    header: list[str],
    row: list[object],
    canonical: str,
    observed_name: str,
) -> dict[str, str]:
    values = {header[index]: row[index] if index < len(row) else "" for index in range(len(header))}
    lower_headers = {key.lower(): key for key in header}

    if "wt_mean" in lower_headers and "ko_mean" in lower_headers:
        control_mean = _as_float(values.get(lower_headers["wt_mean"]))
        case_mean = _as_float(values.get(lower_headers["ko_mean"]))
        log2fc = _as_float(values.get(lower_headers.get("log2fc", "")))
        p_value = _as_float(values.get(lower_headers.get("p_raw", ""))) or _as_float(values.get(lower_headers.get("p_log", "")))
        fdr = _as_float(values.get(lower_headers.get("fdr_raw", ""))) or _as_float(values.get(lower_headers.get("fdr_log", "")))
        note = "whole-lung KO/PH-like columns compared with WT/control columns"
    else:
        sample_headers = [
            key
            for key in header
            if key and not re.search(r"mean|log2fc|p_|fdr|t test", key, re.IGNORECASE)
        ]
        control_cols = list(dict.fromkeys(key for key in sample_headers if re.search(r"control.*mk|wt", key, re.IGNORECASE)))
        case_cols = list(dict.fromkeys(key for key in sample_headers if re.search(r"ph.*mk|ko", key, re.IGNORECASE)))
        control_vals = [_as_float(values.get(key)) for key in control_cols]
        case_vals = [_as_float(values.get(key)) for key in case_cols]
        control_vals = [value for value in control_vals if value is not None]
        case_vals = [value for value in case_vals if value is not None]
        control_mean = _mean(control_vals)
        case_mean = _mean(case_vals)
        log2fc = _safe_log2fc(case_mean, control_mean)
        p_value = _as_float(values.get("t test"))
        fdr = None
        note = f"computed from columns: case={','.join(case_cols)}; control={','.join(control_cols)}"

    return {
        "source_file": source_file,
        "sheet": sheet,
        "metabolite": canonical,
        "matched_name": observed_name,
        "status": "found",
        "control_mean": _format_number(control_mean),
        "case_mean": _format_number(case_mean),
        "log2fc_case_vs_control": _format_number(log2fc),
        "p_value": _format_number(p_value),
        "fdr": _format_number(fdr),
        "note": note,
    }


def _as_float(value: object) -> float | None:
    if value is None or value == "":
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(number):
        return None
    return number


def _mean(values: list[float]) -> float | None:
    if not values:
        return None
    return sum(values) / len(values)


def _safe_log2fc(case_mean: float | None, control_mean: float | None) -> float | None:
    if case_mean is None or control_mean is None:
        return None
    return math.log2((case_mean + 1e-9) / (control_mean + 1e-9))


def _format_number(value: float | None) -> str:
    if value is None:
        return ""
    return f"{value:.4g}"


def _write_dict_rows(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _render_evidence_markdown(
    generated: str,
    seurat_csv: Path,
    seurat_status: str,
    public_de_csv: Path,
    public_de_status: str,
    metabolite_csv: Path,
    metabolite_status: str,
) -> str:
    lines = [
        "# Cycle Evidence Package",
        "",
        f"Generated: {generated}",
        "",
        "This package is generated before PI briefing and hypothesis generation. Agents must treat these",
        "tables as direct local evidence when status is completed, and must explicitly label missing",
        "or identifier-limited rows as evidence gaps rather than negative biological findings.",
        "",
        "## Seurat MK/Platelet Priority Gene Query",
        "",
        f"Status: {seurat_status}",
        f"CSV: {seurat_csv}",
        "",
    ]
    lines.extend(_markdown_table_preview(seurat_csv, max_rows=30))
    lines.extend(
        [
            "",
            "## Public Dataset DE Extraction: GSE289322",
            "",
            f"Status: {public_de_status}",
            f"CSV: {public_de_csv}",
            "",
        ]
    )
    lines.extend(_markdown_table_preview(public_de_csv, max_rows=25))
    lines.extend(
        [
            "",
            "## Whole-Lung and MK Metabolite Cross-check",
            "",
            f"Status: {metabolite_status}",
            f"CSV: {metabolite_csv}",
            "",
        ]
    )
    lines.extend(_markdown_table_preview(metabolite_csv, max_rows=40))
    lines.extend(
        [
            "",
            "## How Agents Should Use This Package",
            "",
            "- Prioritize hypotheses whose mediator genes are matched in Seurat, MK-expressed, and PH-up in MKs.",
            "- Treat public DE rows marked as identifier-limited as unresolved, not as absent expression.",
            "- Treat missing spermidine/spermine or adenosine rows as product-level evidence gaps.",
            "- Do not generate EV, coagulation, or ECM hypotheses unless their candidate genes are supported",
            "  by the Seurat query or explicitly framed as unvalidated alternatives.",
        ]
    )
    return "\n".join(lines).strip() + "\n"


def _markdown_table_preview(path: Path, max_rows: int) -> list[str]:
    if not path.exists():
        return ["[No table written.]"]
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames or []
        rows = list(reader)[:max_rows]
    if not fieldnames:
        return ["[Empty table.]"]
    selected_fields = _preview_fields(fieldnames)
    lines = [
        "| " + " | ".join(selected_fields) + " |",
        "| " + " | ".join("---" for _ in selected_fields) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(_md_cell(row.get(field, "")) for field in selected_fields) + " |")
    return lines


def _preview_fields(fieldnames: list[str]) -> list[str]:
    preferred_sets = [
        [
            "gene_symbol",
            "status",
            "mk_pct_expr",
            "mk_enrichment_log2",
            "ph_vs_control_mk_log2",
            "ph_mk_pct_expr",
            "control_mk_pct_expr",
            "ph_vs_control_mk_p_value",
        ],
        [
            "source_file",
            "sheet",
            "metabolite",
            "status",
            "control_mean",
            "case_mean",
            "log2fc_case_vs_control",
            "fdr",
        ],
        [
            "query_gene",
            "matched_identifier",
            "log2fc_case_vs_control",
            "p_value_approx",
            "fdr_approx",
            "note",
        ],
    ]
    for preferred in preferred_sets:
        selected = [field for field in preferred if field in fieldnames]
        if len(selected) >= 3:
            return selected
    return fieldnames[: min(8, len(fieldnames))]


def _md_cell(value: str) -> str:
    text = str(value or "").replace("\n", " ").replace("|", "/")
    if len(text) > 80:
        return text[:77] + "..."
    return text
