from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import json

from .agents import AgentRunner, AgentSpec, ChatClient
from .config import SystemConfig, TEMPLATE_FILES, read_required_text
from .data_context import build_data_context, write_data_context
from .evidence_package import build_evidence_package
from .metabolic_context import build_metabolic_context
from .public_dataset_analysis import build_public_dataset_analysis_context
from .public_dataset_context import build_public_dataset_context


MAX_CONTEXT_CHARS = 18000
MAX_AGENT_BUNDLE_CHARS = 80000
MAX_REVIEW_BUNDLE_CHARS = 60000
MAX_SINGLE_OUTPUT_CHARS = 24000
MAX_METABOLIC_CONTEXT_CHARS = 32000
MAX_GENERATION_PI_BRIEF_CHARS = 9000
MAX_GENERATION_DATA_CONTEXT_CHARS = 8000
MAX_GENERATION_METABOLIC_CONTEXT_CHARS = 16000
MAX_PUBLIC_DATASET_CONTEXT_CHARS = 24000
MAX_PUBLIC_DATASET_ANALYSIS_CHARS = 24000
MAX_GENERATION_PUBLIC_DATASET_CHARS = 12000
DEFAULT_GENERATION_MAX_TOKENS = 65536
DEFAULT_PI_MAX_TOKENS = 16384
MIN_GENERATION_OUTPUT_CHARS = 500

GENERATION_FOCI = [
    "paracrine ligand-receptor mechanisms involving endothelial or smooth muscle recipient cells",
    "metabolic and extracellular vesicle mechanisms grounded in metabolomics or MK cargo",
    "thrombo-inflammatory, ECM, immune remodeling, and spatial niche mechanisms",
    "mechanisms that explain hypoxia specificity and avoid generic inflammation-only claims",
]

REFLECTION_MODES = [
    "mechanistic plausibility, MK specificity, and hypoxia specificity",
    "evidence grading, direct data support, literature separation, and overinterpretation risks",
    "experimental design, falsifiability, controls, and feasibility",
]


@dataclass(frozen=True)
class WorkflowOptions:
    cycle_id: int = 1
    generation_agents: int = 3
    reflection_agents: int = 3
    parallelism: int = 1
    initial_instruction: str = ""
    rebuild_context: bool = False
    rebuild_metabolic_context: bool = False
    rebuild_public_dataset_context: bool = False
    fetch_kegg: bool = True
    fetch_pubmed: bool = True
    fetch_public_datasets: bool = True
    analyze_public_datasets: bool = False
    reuse_existing_public_analyses: bool = False
    resume_existing: bool = False
    max_metabolites: int = 30
    max_public_datasets: int = 8
    max_public_analyses: int = 3
    max_public_download_mb: int = 1024
    build_evidence_package: bool = True


class MultiAgentWorkflow:
    def __init__(self, config: SystemConfig, client: ChatClient) -> None:
        self.config = config
        self.root = config.root
        self.output_dir = config.output_dir
        self.runner = AgentRunner(config.root, client, config.model)
        self.resume_existing_outputs = False
        self.resume_after: datetime | None = None

    def run_cycle(self, options: WorkflowOptions) -> Path:
        cycle_dir = self.output_dir / f"cycle_{options.cycle_id:03d}"
        cycle_dir.mkdir(parents=True, exist_ok=True)
        manifest_path = cycle_dir / "manifest.json"
        previous_manifest = self._load_manifest(manifest_path) if options.resume_existing else {}
        self.resume_existing_outputs = options.resume_existing
        self.resume_after = self._parse_datetime(previous_manifest.get("started")) if previous_manifest else None

        data_context_path = self.output_dir / "data_context.md"
        if options.rebuild_context or not data_context_path.exists():
            data_context_path = write_data_context(self.root, self.output_dir)
        data_context = data_context_path.read_text(encoding="utf-8")

        metabolic_context_path = self.output_dir / "metabolic_context.md"
        if options.rebuild_context or options.rebuild_metabolic_context or not metabolic_context_path.exists():
            metabolic_context_path = build_metabolic_context(
                self.root,
                self.output_dir,
                fetch_kegg=options.fetch_kegg,
                fetch_pubmed=options.fetch_pubmed,
                max_metabolites=options.max_metabolites,
            )
        metabolic_context = metabolic_context_path.read_text(encoding="utf-8")

        evidence_package = None
        if options.build_evidence_package:
            evidence_package = build_evidence_package(self.root, self.output_dir)
            data_context = data_context.rstrip() + "\n\n" + evidence_package.text.strip() + "\n"

        previous_feedback = self._load_previous_feedback(options.cycle_id)
        templates = {
            key: read_required_text(self.root, filename)
            for key, filename in TEMPLATE_FILES.items()
        }

        manifest = {
            "cycle_id": options.cycle_id,
            "started": previous_manifest.get("started") or datetime.now().isoformat(timespec="seconds"),
            "resumed_at": datetime.now().isoformat(timespec="seconds") if options.resume_existing else None,
            "model": self.config.model,
            "dry_run": self.config.dry_run,
            "generation_agents": options.generation_agents,
            "reflection_agents": options.reflection_agents,
            "parallelism": options.parallelism,
            "data_context": str(data_context_path),
            "metabolic_context": str(metabolic_context_path),
            "fetch_kegg": options.fetch_kegg,
            "fetch_pubmed": options.fetch_pubmed,
            "fetch_public_datasets": options.fetch_public_datasets,
            "analyze_public_datasets": options.analyze_public_datasets,
            "reuse_existing_public_analyses": options.reuse_existing_public_analyses,
            "resume_existing": options.resume_existing,
            "max_public_datasets": options.max_public_datasets,
            "max_public_analyses": options.max_public_analyses,
            "max_public_download_mb": options.max_public_download_mb,
            "evidence_package": str(evidence_package.path) if evidence_package else None,
        }
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

        pi_brief = self._run_pi_brief(
            options,
            data_context,
            metabolic_context,
            previous_feedback,
            templates["pi_to_generation"],
            cycle_dir,
        )

        public_dataset_context_path = build_public_dataset_context(
            self.root,
            self.output_dir,
            pi_brief=pi_brief,
            enabled=options.fetch_public_datasets,
            max_results=options.max_public_datasets,
        )
        public_dataset_context = public_dataset_context_path.read_text(encoding="utf-8")
        manifest["public_dataset_context"] = str(public_dataset_context_path)

        public_dataset_analysis_path = build_public_dataset_analysis_context(
            self.root,
            self.output_dir,
            enabled=options.analyze_public_datasets or options.reuse_existing_public_analyses,
            max_datasets=options.max_public_analyses,
            max_download_mb=options.max_public_download_mb,
            reuse_existing_only=options.reuse_existing_public_analyses,
        )
        public_dataset_analysis_context = public_dataset_analysis_path.read_text(encoding="utf-8")
        manifest["public_dataset_analysis_context"] = str(public_dataset_analysis_path)
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

        public_dataset_output = self._run_agent(
            AgentSpec(
                key="public_dataset",
                name="Public Dataset Agent",
                prompt_key="public_dataset",
                temperature=0.1,
                system_note=(
                    "Use only the provided Public Dataset Discovery Context. Do not claim that a public "
                    "dataset was downloaded or reanalyzed unless the provided context explicitly says so."
                ),
            ),
            self._public_dataset_user_message(
                data_context,
                metabolic_context,
                public_dataset_context,
                public_dataset_analysis_context,
                pi_brief,
            ),
            cycle_dir / "public_dataset_agent.md",
        )

        generation_outputs = self._run_generation_agents(
            options,
            data_context,
            metabolic_context,
            public_dataset_context,
            public_dataset_analysis_context,
            public_dataset_output,
            pi_brief,
            templates,
            cycle_dir,
        )
        self._assert_generation_outputs(generation_outputs, cycle_dir)
        generation_bundle = self._write_bundle(
            cycle_dir / "generation_all.md",
            generation_outputs,
            "Generation Agent Outputs",
        )

        tool_output = self._run_agent(
            AgentSpec(
                key="tool_use",
                name="Tool Use Agent",
                prompt_key="tool_use",
                temperature=0.1,
                system_note=(
                    "Use only the local data context provided in this run unless external evidence is "
                    "explicitly included in the user message. Do not claim that PubMed, KEGG, or public "
                    "datasets were queried when no retrieved results are present."
                ),
            ),
            self._tool_user_message(
                data_context,
                metabolic_context,
                public_dataset_context,
                public_dataset_analysis_context,
                public_dataset_output,
                pi_brief,
                generation_bundle,
            ),
            cycle_dir / "tool_use_agent.md",
        )

        proximity_output = self._run_agent(
            AgentSpec(key="proximity", name="Proximity Check Agent", prompt_key="proximity", temperature=0.1),
            self._proximity_user_message(pi_brief, generation_bundle),
            cycle_dir / "proximity_check_agent.md",
        )

        reflection_outputs = self._run_reflection_agents(
            options,
            pi_brief,
            generation_bundle,
            tool_output,
            public_dataset_output,
            proximity_output,
            cycle_dir,
        )
        reflection_bundle = self._write_bundle(
            cycle_dir / "reflection_all.md",
            reflection_outputs,
            "Reflection Agent Outputs",
        )

        ranking_output = self._run_agent(
            AgentSpec(
                key="ranking",
                name="Ranking Agent",
                prompt_key="ranking",
                temperature=0.1,
                max_tokens=self.config.pi_max_tokens or DEFAULT_PI_MAX_TOKENS,
            ),
            self._ranking_user_message(
                pi_brief,
                metabolic_context,
                public_dataset_context,
                public_dataset_analysis_context,
                public_dataset_output,
                generation_bundle,
                tool_output,
                proximity_output,
                reflection_bundle,
            ),
            cycle_dir / "ranking_agent.md",
        )

        meta_output = self._run_agent(
            AgentSpec(
                key="meta_review",
                name="Meta-review Agent",
                prompt_key="meta_review",
                temperature=0.1,
                max_tokens=self.config.pi_max_tokens or DEFAULT_PI_MAX_TOKENS,
            ),
            self._meta_user_message(pi_brief, generation_bundle, tool_output, public_dataset_output, proximity_output, reflection_bundle, ranking_output),
            cycle_dir / "meta_review_agent.md",
        )

        evolution_output = self._run_agent(
            AgentSpec(
                key="evolution",
                name="Evolution Agent",
                prompt_key="evolution",
                temperature=0.2,
                max_tokens=self.config.pi_max_tokens or DEFAULT_PI_MAX_TOKENS,
            ),
            self._evolution_user_message(
                pi_brief,
                generation_bundle,
                tool_output,
                public_dataset_output,
                proximity_output,
                reflection_bundle,
                ranking_output,
                meta_output,
            ),
            cycle_dir / "evolution_agent.md",
        )

        pi_feedback = self._run_agent(
            AgentSpec(
                key="pi_final",
                name="PI Agent Final Feedback",
                prompt_key="pi",
                temperature=0.1,
                max_tokens=self.config.pi_max_tokens or DEFAULT_PI_MAX_TOKENS,
            ),
            self._pi_feedback_user_message(
                options,
                data_context,
                metabolic_context,
                public_dataset_context,
                public_dataset_analysis_context,
                public_dataset_output,
                pi_brief,
                generation_bundle,
                tool_output,
                proximity_output,
                reflection_bundle,
                ranking_output,
                meta_output,
                evolution_output,
            ),
            cycle_dir / "pi_final_feedback.md",
        )

        self._write_cycle_summary(
            cycle_dir,
            pi_brief,
            metabolic_context,
            public_dataset_context,
            public_dataset_analysis_context,
            public_dataset_output,
            generation_bundle,
            tool_output,
            proximity_output,
            reflection_bundle,
            ranking_output,
            meta_output,
            evolution_output,
            pi_feedback,
        )
        return cycle_dir

    def _run_agent(self, spec: AgentSpec, user_message: str, output_path: Path) -> str:
        if self._can_reuse_output(output_path):
            return output_path.read_text(encoding="utf-8").strip()
        if self.resume_existing_outputs:
            self.resume_existing_outputs = False
        return self.runner.run(spec, user_message, output_path)

    def _can_reuse_output(self, output_path: Path) -> bool:
        if not self.resume_existing_outputs or not output_path.exists():
            return False
        text = output_path.read_text(encoding="utf-8").strip()
        if not text:
            return False
        if self._output_was_truncated(output_path):
            return False
        if self.resume_after is None:
            return True
        modified = datetime.fromtimestamp(output_path.stat().st_mtime)
        return modified >= self.resume_after

    @staticmethod
    def _output_was_truncated(output_path: Path) -> bool:
        meta_path = output_path.with_suffix(output_path.suffix + ".meta.json")
        if not meta_path.exists():
            return False
        try:
            metadata = json.loads(meta_path.read_text(encoding="utf-8"))
        except Exception:
            return False
        return metadata.get("finish_reason") == "length"

    @staticmethod
    def _load_manifest(path: Path) -> dict:
        if not path.exists():
            return {}
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return {}

    @staticmethod
    def _parse_datetime(value: object) -> datetime | None:
        if not isinstance(value, str) or not value:
            return None
        try:
            return datetime.fromisoformat(value)
        except ValueError:
            return None

    def _run_pi_brief(
        self,
        options: WorkflowOptions,
        data_context: str,
        metabolic_context: str,
        previous_feedback: str,
        template: str,
        cycle_dir: Path,
    ) -> str:
        user_message = f"""
Cycle ID: {options.cycle_id}

Task:
Prepare the structured research brief for Generation Agents for this cycle.

Initial user instruction:
{options.initial_instruction or "Use the project design and available user-provided data."}

Previous cycle PI feedback:
{previous_feedback or "None. This is the first cycle or no previous PI feedback was found."}

Available user-provided data context:
{self._clip(data_context, MAX_CONTEXT_CHARS, "data context")}

Available metabolomics-to-mechanism evidence context:
{self._clip(metabolic_context, MAX_METABOLIC_CONTEXT_CHARS, "metabolic context")}

Required handoff template:
{template}

Additional PI constraint:
Include a "Public dataset search tasks" section in the PI brief. These tasks should be broad enough
to search public repositories for validation datasets and should not be limited to scRNA-seq. Include
keywords for disease/perturbation, tissue, cell types, and modalities such as bulk RNA-seq,
single-cell or single-nucleus RNA-seq, spatial transcriptomics, proteomics, metabolomics, and
microarray when relevant. The downstream Public Dataset Discovery Module will use this section for
programmatic repository search.

Require a dedicated metabolomics-driven hypothesis class in this cycle. At least 40% of generated
hypotheses should follow the chain: differential metabolite A -> KEGG direct enzyme or same-pathway
neighbor enzyme/gene -> candidate metabolic enzyme gene B -> MK/platelet expression or enrichment
in seurat_merged.rds -> directional downstream biology -> vascular remodeling phenotype.
The PI brief should ask for direction-level hypotheses rather than fully resolved causal routes.
For example, it is sufficient to say that MK AMD1 may reshape methionine/SAM/polyamine metabolism,
and that this may influence T-helper/Th17-like immune tone, perivascular inflammation, or direct
vascular-wall activation. Do not require agents to choose one exact metabolite product, cytokine,
recipient subtype, or EndMT mechanism unless direct evidence in the provided context supports it.
Require Generation Agents to show a concise "Direction-level reasoning summary" for each hypothesis,
not only a checklist. The summary should connect: direct data anchor -> biological interpretation ->
MK-linked mediator/enzyme/pathway class -> plausible downstream axis -> broad remodeling phenotype
-> key uncertainty. This is an evidence-linked rationale for review, not private chain-of-thought.
Keep the requested volume realistic: broad cycle coverage should be distributed across generation
agents, with roughly 3-6 complete, reasoning-rich hypotheses per branch rather than a single agent
being asked to produce an oversized 10-12 hypothesis manuscript.
When writing metabolomics priorities, use the "Mechanism-Ready Hypothesis Shortlist" from the
metabolic context as the authoritative source. Do not let previous-cycle named metabolite priorities
override shortlist rows that have positive MK enrichment, PH-up MK shift, and strong non-generic
mechanism cues. The PI brief should explicitly preserve the top mechanism-ready chains as candidates
for the dedicated metabolic generation agent.
For mechanism-ready metabolic chains, the PI brief should ask agents to define a plausible
downstream axis, not a final multi-hop mechanism. Useful axis labels include immune-mediated,
direct vascular-wall, EV/stromal, or unresolved. Agents may mention candidate bridges such as
Th17-like T-cell activity, macrophage/monocyte activation, endothelial activation, smooth-muscle
activation, medial remodeling, vascular stiffness, or stromal remodeling, but these should remain
candidates unless directly supported. Do not require a Bridge Convergence Matrix in this cycle.
Instead, ask for a short "candidate downstream axes" note that names 2-4 plausible routes and marks
which one is only a working model. If previous feedback names a recipient cell, release route, or
bridge model for a metabolic chain, treat it as one possible example rather than the default final
mechanism.
""".strip()
        return self._run_agent(
            AgentSpec(
                key="pi_brief",
                name="PI Agent Brief",
                prompt_key="pi",
                temperature=0.2,
                max_tokens=self.config.pi_max_tokens or DEFAULT_PI_MAX_TOKENS,
            ),
            user_message,
            cycle_dir / "pi_research_brief.md",
        )

    def _run_generation_agents(
        self,
        options: WorkflowOptions,
        data_context: str,
        metabolic_context: str,
        public_dataset_context: str,
        public_dataset_analysis_context: str,
        public_dataset_output: str,
        pi_brief: str,
        templates: dict[str, str],
        cycle_dir: Path,
    ) -> dict[str, str]:
        count = max(1, options.generation_agents)
        tasks: list[tuple[AgentSpec, str, Path]] = []
        metabolic_spec = AgentSpec(
            key="generation_metabolic",
            name="Metabolic Hypothesis Generation Agent",
            prompt_key="generation_runtime",
            temperature=0.25,
            max_tokens=self.config.generation_max_tokens or DEFAULT_GENERATION_MAX_TOKENS,
            system_note=(
                "You are the dedicated metabolomics-driven generation branch. Generate only hypotheses "
                "anchored to this chain: differential metabolite A -> KEGG direct enzyme or same-pathway "
                "neighbor enzyme/gene -> candidate enzyme gene B -> MK/platelet expression or enrichment "
                "-> directional downstream biology -> vascular remodeling phenotype. "
                "Keep mechanisms at direction level unless direct evidence supports finer resolution. "
                "Never return an empty response. If evidence is incomplete or instructions conflict, "
                "produce the strongest directional hypotheses and label gaps clearly."
            ),
        )
        metabolic_message = f"""
Cycle ID: {options.cycle_id}

PI research brief:
{self._clip(pi_brief, MAX_GENERATION_PI_BRIEF_CHARS, "PI brief")}

Metabolomics-to-mechanism evidence context:
{self._clip(metabolic_context, MAX_GENERATION_METABOLIC_CONTEXT_CHARS, "metabolic context")}

Available user-provided data context:
{self._clip(data_context, MAX_GENERATION_DATA_CONTEXT_CHARS, "data context")}

Public dataset discovery context:
{self._clip(public_dataset_context, MAX_GENERATION_PUBLIC_DATASET_CHARS, "public dataset context")}

Public dataset analysis context:
{self._clip(public_dataset_analysis_context, MAX_GENERATION_PUBLIC_DATASET_CHARS, "public dataset analysis context")}

Public Dataset Agent interpretation:
{self._clip(public_dataset_output, MAX_SINGLE_OUTPUT_CHARS, "public dataset agent output")}

Expected output template:
{templates["generation_to_pi"]}

Instruction:
Generate all reasonably supported, non-redundant metabolomics-driven hypotheses that pass the quality
filter. Do not impose a fixed count. Start from the Mechanism-Ready Hypothesis Shortlist when present:
include the top shortlist rows unless there is a fatal biological flaw; if you skip a top shortlist row,
state the exact reason. If evidence is insufficient for a chain, either exclude it or include it as a
clearly labeled exploratory hypothesis with explicit gaps; do not return an empty response.
Prefer rows with positive MK enrichment, PH-up MK shift, significant PH-vs-control MK p value, and
strong non-generic mechanism cues such as polyamine, S-adenosylmethionine, methionine salvage,
redox/glutathione, retinoid, tryptophan, one-carbon, or arginine/proline biology. Do not substitute
older PI-priority metabolites for a stronger mechanism-ready shortlist row. Every hypothesis must name:
- differential metabolite A, source file/comparison, direction, and log2FC
- KEGG direct compound-enzyme evidence or same-pathway neighbor-gene evidence
- candidate enzyme gene B
- the evidence link type
- whether B is expressed/enriched/differential in MK/platelet cells from Seurat
- PubMed/literature search support if available, or a clearly labeled literature gap
- broad downstream axis: immune-mediated, direct vascular-wall, EV/stromal, or unresolved
- public dataset validation opportunity if any retrieved dataset can test this direction
- candidate downstream routes, without selecting a final route unless direct evidence supports it
- broad vascular remodeling phenotype such as medial activation, muscularization, vascular
  stiffness, endothelial dysfunction, or matrix remodeling
- falsification criterion that tests the metabolite-enzyme-MK-remodeling direction

For every hypothesis, include a "Direction-level reasoning summary" before the detailed chain. Use
4 to 6 compact bullets that explain the scientific logic in order:
- Data anchor: the direct metabolite/KEGG/Seurat/literature observation that starts the hypothesis
- Biological interpretation: what that anchor implies about MK state or metabolic flux
- MK-linked pathway logic: why the named enzyme or pathway class is a plausible causal handle
- Candidate downstream axis: 2-4 plausible routes, keeping specific mediators or cell subtypes
  as examples rather than final claims
- Remodeling logic: how the axis could influence broad vascular remodeling phenotypes
- Key uncertainty: the single weakest link or assumption
Keep this as auditable scientific rationale tied to evidence; do not output hidden deliberation or
unsupported speculation.

Do not over-resolve the mechanism. Avoid writing that AMD1 acts specifically through spermidine,
Th17, IL-17, EndMT, or any other named mediator/subset as the final path unless the provided
evidence directly supports that specificity. It is acceptable and preferred to write broader claims
such as: MK AMD1 may affect methionine/SAM/polyamine metabolism, which may influence T-helper/
Th17-like or other perivascular immune programs, contributing to medial activation and vascular
stiffness.

Include a "Candidate Downstream Axes" block for every hypothesis:
- Plausible axes: 2-4 broad routes such as immune-mediated, direct vascular-wall, EV/stromal, or unresolved
- Working model: the route that currently seems most useful to test, clearly labeled provisional
- Specific examples: optional examples such as SAM, spermidine, Th17-like tone, endothelial
  activation, medial activation, or vascular stiffness; do not treat examples as settled mechanisms
- MK-origin gap: what is not yet proven about MK source, release, proximity, or transfer
- Falsification: perturb MK enzyme/metabolite and test whether the broad remodeling phenotype changes
""".strip()
        tasks.append((metabolic_spec, metabolic_message, cycle_dir / "generation_agent_metabolic.md"))

        for index in range(count):
            focus = GENERATION_FOCI[index % len(GENERATION_FOCI)]
            spec = AgentSpec(
                key=f"generation_{index + 1}",
                name=f"Generation Agent {index + 1}",
                prompt_key="generation_runtime",
                temperature=0.35 + min(index, 3) * 0.05,
                max_tokens=self.config.generation_max_tokens or DEFAULT_GENERATION_MAX_TOKENS,
                system_note=f"Generate a distinct hypothesis set with emphasis on: {focus}.",
            )
            user_message = f"""
Cycle ID: {options.cycle_id}

PI research brief:
{self._clip(pi_brief, MAX_GENERATION_PI_BRIEF_CHARS, "PI brief")}

Available user-provided data context:
{self._clip(data_context, MAX_GENERATION_DATA_CONTEXT_CHARS, "data context")}

Metabolomics-to-mechanism evidence context:
{self._clip(metabolic_context, MAX_GENERATION_METABOLIC_CONTEXT_CHARS, "metabolic context")}

Public dataset discovery context:
{self._clip(public_dataset_context, MAX_GENERATION_PUBLIC_DATASET_CHARS, "public dataset context")}

Public dataset analysis context:
{self._clip(public_dataset_analysis_context, MAX_GENERATION_PUBLIC_DATASET_CHARS, "public dataset analysis context")}

Public Dataset Agent interpretation:
{self._clip(public_dataset_output, MAX_SINGLE_OUTPUT_CHARS, "public dataset agent output")}

Expected output template:
{templates["generation_to_pi"]}

Instruction:
Generate hypotheses that are distinct from other likely Generation Agent outputs. Clearly label direct
user-data support versus inference. Do not fabricate citations or data. Include at least one
metabolomics-driven hypothesis if your focus permits it, and do not ignore the metabolic evidence package.
Use retrieved public dataset metadata as validation opportunity or contextual support; do not claim
expression matrices or raw samples were analyzed unless the public dataset context explicitly says so.
Generate all reasonably supported, non-redundant hypotheses that match your assigned focus and pass
the quality filter. Do not impose a fixed count. If evidence is incomplete or constraints conflict,
label the gap and still produce the strongest testable hypotheses; do not return an empty response.
For each hypothesis, add a compact "Direction-level reasoning summary" that explains the data
anchor, biological interpretation, mediator/pathway class, plausible downstream axis, broad
remodeling phenotype, and key uncertainty. This should read like an evidence-linked scientific
rationale, not a checklist and not private chain-of-thought.
For any metabolomics-driven hypothesis, keep the downstream mechanism at direction level unless
direct evidence supports finer resolution. Name 2-4 candidate downstream axes rather than forcing a
single winning bridge. Do not over-specify a T-cell subset, cytokine, vascular recipient, or EndMT
route unless it is clearly supported; treat examples as working models.
""".strip()
            tasks.append((spec, user_message, cycle_dir / f"generation_agent_{index + 1}.md"))
        return self._run_agent_tasks(tasks, max_workers=max(1, options.parallelism), continue_on_error=True)

    def _run_reflection_agents(
        self,
        options: WorkflowOptions,
        pi_brief: str,
        generation_bundle: str,
        tool_output: str,
        public_dataset_output: str,
        proximity_output: str,
        cycle_dir: Path,
    ) -> dict[str, str]:
        count = max(1, options.reflection_agents)
        tasks: list[tuple[AgentSpec, str, Path]] = []
        for index in range(count):
            mode = REFLECTION_MODES[index % len(REFLECTION_MODES)]
            spec = AgentSpec(
                key=f"reflection_{index + 1}",
                name=f"Reflection Agent {index + 1}",
                prompt_key="reflection",
                temperature=0.15,
                system_note=f"Review mode for this agent: {mode}.",
            )
            user_message = f"""
Cycle ID: {options.cycle_id}

PI research brief:
{pi_brief}

Generated hypotheses:
{self._clip(generation_bundle, MAX_AGENT_BUNDLE_CHARS, "generated hypotheses")}

Tool Use Agent evidence summary:
{self._clip(tool_output, MAX_SINGLE_OUTPUT_CHARS, "tool output")}

Public Dataset Agent evidence summary:
{self._clip(public_dataset_output, MAX_SINGLE_OUTPUT_CHARS, "public dataset output")}

Proximity Check Agent output:
{self._clip(proximity_output, MAX_SINGLE_OUTPUT_CHARS, "proximity output")}

Instruction:
Critique each hypothesis according to your assigned review mode while still covering the required
Reflection Agent output format. Be strict about separating direct evidence, retrieved public dataset
metadata, downloaded/reanalyzed public data, literature, and inference.
""".strip()
            tasks.append((spec, user_message, cycle_dir / f"reflection_agent_{index + 1}.md"))
        return self._run_agent_tasks(tasks, max_workers=max(1, options.parallelism))

    def _run_agent_tasks(
        self,
        tasks: list[tuple[AgentSpec, str, Path]],
        max_workers: int,
        *,
        continue_on_error: bool = False,
    ) -> dict[str, str]:
        if max_workers <= 1 or len(tasks) <= 1:
            outputs: dict[str, str] = {}
            for spec, message, path in tasks:
                try:
                    outputs[spec.key] = self._run_agent(spec, message, path)
                except Exception as exc:
                    if not continue_on_error:
                        raise
                    outputs[spec.key] = self._write_agent_failure(spec, path, exc)
            return outputs

        outputs: dict[str, str] = {}
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_map = {
                executor.submit(self._run_agent, spec, message, path): (spec, path)
                for spec, message, path in tasks
            }
            for future in as_completed(future_map):
                spec, path = future_map[future]
                try:
                    outputs[spec.key] = future.result()
                except Exception as exc:
                    if not continue_on_error:
                        raise
                    outputs[spec.key] = self._write_agent_failure(spec, path, exc)
        return dict(sorted(outputs.items()))

    @staticmethod
    def _write_agent_failure(spec: AgentSpec, output_path: Path, exc: Exception) -> str:
        content = (
            f"# {spec.name} Failed\n\n"
            f"Agent key: {spec.key}\n\n"
            f"Error type: {type(exc).__name__}\n\n"
            f"Error message: {exc}\n\n"
            "This branch failed, but the workflow kept other generation outputs so the cycle can continue "
            "when at least one usable hypothesis set exists.\n"
        )
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding="utf-8")
        output_path.with_suffix(output_path.suffix + ".meta.json").write_text(
            json.dumps(
                {
                    "agent_key": spec.key,
                    "prompt_key": spec.prompt_key,
                    "failed": True,
                    "error_type": type(exc).__name__,
                    "error_message": str(exc),
                    "content_chars": 0,
                },
                indent=2,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        return content

    def _public_dataset_user_message(
        self,
        data_context: str,
        metabolic_context: str,
        public_dataset_context: str,
        public_dataset_analysis_context: str,
        pi_brief: str,
    ) -> str:
        return f"""
Request addressed:
Evaluate programmatically retrieved public dataset metadata for the current PI research brief.

PI research brief:
{self._clip(pi_brief, MAX_SINGLE_OUTPUT_CHARS, "PI brief")}

Public Dataset Discovery Context:
{self._clip(public_dataset_context, MAX_PUBLIC_DATASET_CONTEXT_CHARS, "public dataset context")}

Public Dataset Analysis Context:
{self._clip(public_dataset_analysis_context, MAX_PUBLIC_DATASET_ANALYSIS_CHARS, "public dataset analysis context")}

Available local data context:
{self._clip(data_context, MAX_CONTEXT_CHARS, "data context")}

Available metabolomics-to-mechanism evidence context:
{self._clip(metabolic_context, MAX_METABOLIC_CONTEXT_CHARS, "metabolic context")}

Instruction:
Rank retrieved public datasets and any completed public-dataset analyses by their usefulness for
validating MK-hypoxia-vascular remodeling hypotheses. Consider transcriptomics, single-cell/
single-nucleus, spatial, proteomics, metabolomics, and other omics datasets. Clearly separate
metadata-level relevance, downloaded processed-matrix analysis, and evidence that would still
require manual reanalysis. Do not invent accessions or claim any dataset was analyzed beyond the
provided context.
""".strip()

    def _tool_user_message(
        self,
        data_context: str,
        metabolic_context: str,
        public_dataset_context: str,
        public_dataset_analysis_context: str,
        public_dataset_output: str,
        pi_brief: str,
        generation_bundle: str,
    ) -> str:
        return f"""
Request addressed:
Inspect local user-provided data context and generated requests for downstream evidence needs.

PI research brief:
{self._clip(pi_brief, MAX_SINGLE_OUTPUT_CHARS, "PI brief")}

Generated hypotheses and tool requests:
{self._clip(generation_bundle, MAX_AGENT_BUNDLE_CHARS, "generated hypotheses")}

Available local data context:
{self._clip(data_context, MAX_CONTEXT_CHARS, "data context")}

Available metabolomics-to-mechanism evidence context:
{self._clip(metabolic_context, MAX_METABOLIC_CONTEXT_CHARS, "metabolic context")}

Public dataset discovery context:
{self._clip(public_dataset_context, MAX_PUBLIC_DATASET_CONTEXT_CHARS, "public dataset context")}

Public dataset analysis context:
{self._clip(public_dataset_analysis_context, MAX_PUBLIC_DATASET_ANALYSIS_CHARS, "public dataset analysis context")}

Public Dataset Agent interpretation:
{self._clip(public_dataset_output, MAX_SINGLE_OUTPUT_CHARS, "public dataset output")}

Instruction:
Summarize what can and cannot be supported from the current local data context and metabolic evidence
package. For metabolomics hypotheses, explicitly assess each metabolite -> KEGG enzyme -> enzyme gene ->
MK expression -> literature-hit chain, including same-pathway neighbor-gene links when direct
compound-enzyme evidence is absent.
Also assess whether the evidence supports only a broad downstream axis or a more specific route.
Where relevant, distinguish claims that were checked in processed public matrices from claims that
could only be checked in retrieved metadata. Do not treat metadata as expression-level support.
For each top metabolic chain, list plausible candidate downstream axes rather than forcing a final
bridge: direct vascular-wall, immune-mediated/T-helper-like, macrophage/monocyte or neutrophil
inflammatory, EV/stromal, or unresolved. Treat specific examples such as Th17, IL-17, spermidine,
or EndMT as provisional unless direct evidence supports that specificity. Mark missing evidence
explicitly.
""".strip()

    def _proximity_user_message(self, pi_brief: str, generation_bundle: str) -> str:
        return f"""
PI research brief:
{self._clip(pi_brief, MAX_SINGLE_OUTPUT_CHARS, "PI brief")}

Generated hypotheses to cluster:
{self._clip(generation_bundle, MAX_AGENT_BUNDLE_CHARS, "generated hypotheses")}

Instruction:
Cluster, de-duplicate, and identify complementary or competing hypotheses before review and ranking.
""".strip()

    def _ranking_user_message(
        self,
        pi_brief: str,
        metabolic_context: str,
        public_dataset_context: str,
        public_dataset_analysis_context: str,
        public_dataset_output: str,
        generation_bundle: str,
        tool_output: str,
        proximity_output: str,
        reflection_bundle: str,
    ) -> str:
        return f"""
PI research brief:
{self._clip(pi_brief, MAX_SINGLE_OUTPUT_CHARS, "PI brief")}

Generated hypotheses:
{self._clip(generation_bundle, MAX_AGENT_BUNDLE_CHARS, "generated hypotheses")}

Metabolomics-to-mechanism evidence context:
{self._clip(metabolic_context, MAX_METABOLIC_CONTEXT_CHARS, "metabolic context")}

Public dataset discovery context:
{self._clip(public_dataset_context, MAX_PUBLIC_DATASET_CONTEXT_CHARS, "public dataset context")}

Public dataset analysis context:
{self._clip(public_dataset_analysis_context, MAX_PUBLIC_DATASET_ANALYSIS_CHARS, "public dataset analysis context")}

Public Dataset Agent evidence summary:
{self._clip(public_dataset_output, MAX_SINGLE_OUTPUT_CHARS, "public dataset output")}

Tool Use Agent evidence summary:
{self._clip(tool_output, MAX_SINGLE_OUTPUT_CHARS, "tool output")}

Proximity Check Agent output:
{self._clip(proximity_output, MAX_SINGLE_OUTPUT_CHARS, "proximity output")}

Reflection Agent critiques:
{self._clip(reflection_bundle, MAX_REVIEW_BUNDLE_CHARS, "reflection critiques")}

Instruction:
Rank and compare hypotheses. Penalize hypotheses with weak MK specificity, weak hypoxia specificity,
generic inflammation-only logic, or no feasible falsification test. For metabolomics-driven hypotheses,
reward complete chains with differential metabolite, KEGG direct enzyme or same-pathway neighbor-gene
evidence, MK expression evidence, PH-up MK shift, strong non-generic mechanism cues, and a plausible
directional remodeling mechanism. Reward hypotheses that keep the downstream route appropriately
scoped: broad when the evidence is broad, specific only when direct evidence supports specificity.
Do not penalize a metabolic hypothesis for naming candidate axes rather than a single winning
bridge. Do penalize hypotheses that overstate provisional examples such as spermidine, Th17, IL-17,
or EndMT as established final routes. Penalize generic
housekeeping/glycolysis-only chains even when their metabolite fold change is large.
Also score the quality of the displayed direction-level reasoning: reward hypotheses that explain
how the data anchor leads to the biological interpretation, why the downstream axis is plausible,
which specific details remain unresolved, and what uncertainty could overturn the claim. Penalize
hypotheses that merely list required fields without an evidence-linked rationale.
Reward hypotheses supported by completed processed-matrix public dataset analysis more than
metadata-only validation opportunities. Do not treat public dataset metadata as direct expression or
causal evidence unless analysis results are present.
""".strip()

    def _meta_user_message(
        self,
        pi_brief: str,
        generation_bundle: str,
        tool_output: str,
        public_dataset_output: str,
        proximity_output: str,
        reflection_bundle: str,
        ranking_output: str,
    ) -> str:
        return f"""
PI research brief:
{self._clip(pi_brief, MAX_SINGLE_OUTPUT_CHARS, "PI brief")}

Generated hypotheses:
{self._clip(generation_bundle, MAX_AGENT_BUNDLE_CHARS, "generated hypotheses")}

Tool Use Agent evidence summary:
{self._clip(tool_output, MAX_SINGLE_OUTPUT_CHARS, "tool output")}

Public Dataset Agent evidence summary:
{self._clip(public_dataset_output, MAX_SINGLE_OUTPUT_CHARS, "public dataset output")}

Proximity Check Agent output:
{self._clip(proximity_output, MAX_SINGLE_OUTPUT_CHARS, "proximity output")}

Reflection Agent critiques:
{self._clip(reflection_bundle, MAX_REVIEW_BUNDLE_CHARS, "reflection critiques")}

Ranking Agent output:
{self._clip(ranking_output, MAX_SINGLE_OUTPUT_CHARS, "ranking output")}

Instruction:
Synthesize consensus, disagreement, systemic failure modes, and concrete next-cycle feedback. The
Evolution Agent has not yet run in this cycle, so do not invent evolution results.
""".strip()

    def _evolution_user_message(
        self,
        pi_brief: str,
        generation_bundle: str,
        tool_output: str,
        public_dataset_output: str,
        proximity_output: str,
        reflection_bundle: str,
        ranking_output: str,
        meta_output: str,
    ) -> str:
        return f"""
PI research brief:
{self._clip(pi_brief, MAX_SINGLE_OUTPUT_CHARS, "PI brief")}

Generated hypotheses:
{self._clip(generation_bundle, MAX_AGENT_BUNDLE_CHARS, "generated hypotheses")}

Tool Use Agent evidence summary:
{self._clip(tool_output, MAX_SINGLE_OUTPUT_CHARS, "tool output")}

Public Dataset Agent evidence summary:
{self._clip(public_dataset_output, MAX_SINGLE_OUTPUT_CHARS, "public dataset output")}

Proximity Check Agent output:
{self._clip(proximity_output, MAX_SINGLE_OUTPUT_CHARS, "proximity output")}

Reflection Agent critiques:
{self._clip(reflection_bundle, MAX_REVIEW_BUNDLE_CHARS, "reflection critiques")}

Ranking Agent output:
{self._clip(ranking_output, MAX_SINGLE_OUTPUT_CHARS, "ranking output")}

Meta-review Agent output:
{self._clip(meta_output, MAX_SINGLE_OUTPUT_CHARS, "meta-review output")}

Instruction:
Refine, merge, simplify, or extend only the strongest or most promising hypotheses. Explicitly state
what unsupported claims were removed and what evidence remains missing.
When revising a hypothesis, preserve or add a concise "Direction-level reasoning summary" that makes
the scientific logic visible: data anchor -> biological interpretation -> mediator/pathway class ->
candidate downstream axis -> remodeling phenotype -> key uncertainty.
For metabolic hypotheses that are too thin, extend them by clarifying the broad downstream axis and
validation path, not by forcing a final bridge. Keep details such as exact metabolite product,
T-cell subset, cytokine, receptor route, or EndMT provisional unless directly supported. When
revising a metabolic hypothesis, summarize which downstream axes remain plausible and which evidence
would be needed to resolve them.
When adding public-data support, treat retrieved public datasets as validation opportunities unless
the cycle contains downloaded/reanalyzed results.
""".strip()

    def _pi_feedback_user_message(
        self,
        options: WorkflowOptions,
        data_context: str,
        metabolic_context: str,
        public_dataset_context: str,
        public_dataset_analysis_context: str,
        public_dataset_output: str,
        pi_brief: str,
        generation_bundle: str,
        tool_output: str,
        proximity_output: str,
        reflection_bundle: str,
        ranking_output: str,
        meta_output: str,
        evolution_output: str,
    ) -> str:
        return f"""
Cycle ID: {options.cycle_id}

Task:
Provide the final PI assessment for this cycle and the structured research brief/feedback for the next cycle.

Current cycle PI brief:
{pi_brief}

Available user-provided data context:
{self._clip(data_context, MAX_CONTEXT_CHARS, "data context")}

Available metabolomics-to-mechanism evidence context:
{self._clip(metabolic_context, MAX_METABOLIC_CONTEXT_CHARS, "metabolic context")}

Public dataset discovery context:
{self._clip(public_dataset_context, MAX_PUBLIC_DATASET_CONTEXT_CHARS, "public dataset context")}

Public dataset analysis context:
{self._clip(public_dataset_analysis_context, MAX_PUBLIC_DATASET_ANALYSIS_CHARS, "public dataset analysis context")}

Public Dataset Agent evidence summary:
{self._clip(public_dataset_output, MAX_SINGLE_OUTPUT_CHARS, "public dataset output")}

Generated hypotheses:
{self._clip(generation_bundle, MAX_AGENT_BUNDLE_CHARS, "generated hypotheses")}

Tool Use Agent evidence summary:
{self._clip(tool_output, MAX_SINGLE_OUTPUT_CHARS, "tool output")}

Proximity Check Agent output:
{self._clip(proximity_output, MAX_SINGLE_OUTPUT_CHARS, "proximity output")}

Reflection Agent critiques:
{self._clip(reflection_bundle, MAX_REVIEW_BUNDLE_CHARS, "reflection critiques")}

Ranking Agent output:
{self._clip(ranking_output, MAX_SINGLE_OUTPUT_CHARS, "ranking output")}

Meta-review Agent output:
{self._clip(meta_output, MAX_SINGLE_OUTPUT_CHARS, "meta-review output")}

Evolution Agent output:
{self._clip(evolution_output, MAX_SINGLE_OUTPUT_CHARS, "evolution output")}

Instruction:
Use the PI Agent final output format. Make actionable decisions for each hypothesis, identify data and
literature gaps, and specify exact instructions for the next Generation cycle. Explicitly state which
metabolomics-driven hypotheses have complete or incomplete metabolite -> KEGG enzyme/gene -> MK
expression -> directional downstream axis -> vascular remodeling chains. State whether each
hypothesis is appropriately scoped or over-resolved. Do not turn a current-cycle candidate example
into the required final bridge for the next cycle unless direct evidence supports it. For next-cycle
metabolic instructions, request candidate downstream axes rather than a Bridge Convergence Matrix
unless the user explicitly wants high-resolution bridge adjudication.
For each hypothesis decision, briefly evaluate whether the direction-level reasoning summary was
convincing: did it connect the data anchor, biological interpretation, plausible downstream axis,
remodeling phenotype, and key uncertainty, or did it only list criteria?
For the next cycle, specify whether additional public datasets should be downloaded/reanalyzed,
which accession or source should be prioritized, and what expression/pathway readout should be
tested. Keep metadata support separate from analyzed public-data evidence.
""".strip()

    def _load_previous_feedback(self, cycle_id: int) -> str:
        if cycle_id <= 1:
            return ""
        previous = self.output_dir / f"cycle_{cycle_id - 1:03d}" / "pi_final_feedback.md"
        if previous.exists():
            return previous.read_text(encoding="utf-8")
        return ""

    def _assert_generation_outputs(self, outputs: dict[str, str], cycle_dir: Path) -> None:
        if self.config.dry_run:
            return
        usable = {
            key: text
            for key, text in outputs.items()
            if self._looks_like_hypothesis_output(text)
        }
        if "generation_metabolic" in outputs and "generation_metabolic" not in usable:
            self._write_generation_failure(
                cycle_dir,
                outputs,
                "Dedicated metabolic generation output is empty or lacks hypotheses.",
            )
            raise RuntimeError(
                "Generation failed: the dedicated metabolic generation agent did not produce hypotheses. "
                f"See {cycle_dir / 'generation_failure.md'}."
            )
        if usable:
            return
        self._write_generation_failure(cycle_dir, outputs, "All generation agents returned empty or non-hypothesis outputs.")
        raise RuntimeError(
            "Generation failed: no hypotheses were produced. "
            f"See {cycle_dir / 'generation_failure.md'}."
        )

    @staticmethod
    def _looks_like_hypothesis_output(text: str) -> bool:
        stripped = text.strip()
        if len(stripped) < MIN_GENERATION_OUTPUT_CHARS:
            return False
        markers = (
            "Hypothesis ID",
            "Hypothesis title",
            "Core hypothesis",
            "Mechanistic reasoning summary",
            "Mechanistic chain",
            "H1",
        )
        return any(marker in stripped for marker in markers)

    @staticmethod
    def _write_generation_failure(cycle_dir: Path, outputs: dict[str, str], reason: str) -> None:
        lines = [
            "# Generation Failure",
            "",
            f"Reason: {reason}",
            "",
            "| Agent | Characters written | Looks empty |",
            "|---|---:|---|",
        ]
        for key, text in outputs.items():
            lines.append(f"| {key} | {len(text.strip())} | {'yes' if not text.strip() else 'no'} |")
        lines.extend(
            [
                "",
                "The workflow stopped here so downstream agents do not review an empty hypothesis set.",
                "Common causes are an empty model response, an over-long generation prompt, or a model-side output issue.",
            ]
        )
        (cycle_dir / "generation_failure.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    def _write_bundle(self, path: Path, outputs: dict[str, str], title: str) -> str:
        parts = [f"# {title}"]
        for key, content in outputs.items():
            parts.extend(["", f"## {key}", content.strip()])
        text = "\n".join(parts).strip() + "\n"
        path.write_text(text, encoding="utf-8")
        return text

    def _clip(self, text: str, max_chars: int, label: str) -> str:
        if len(text) <= max_chars:
            return text
        head = max_chars // 2
        tail = max_chars - head
        return (
            text[:head]
            + f"\n\n[... {label} truncated for prompt transport: "
            + f"{len(text) - max_chars} characters omitted. Full text is saved in the cycle output files. ...]\n\n"
            + text[-tail:]
        )

    def _write_cycle_summary(
        self,
        cycle_dir: Path,
        pi_brief: str,
        metabolic_context: str,
        public_dataset_context: str,
        public_dataset_analysis_context: str,
        public_dataset_output: str,
        generation_bundle: str,
        tool_output: str,
        proximity_output: str,
        reflection_bundle: str,
        ranking_output: str,
        meta_output: str,
        evolution_output: str,
        pi_feedback: str,
    ) -> None:
        sections = {
            "PI research brief": pi_brief,
            "Metabolomics-to-mechanism context": metabolic_context,
            "Public dataset discovery context": public_dataset_context,
            "Public dataset analysis context": public_dataset_analysis_context,
            "Public Dataset Agent output": public_dataset_output,
            "Generation outputs": generation_bundle,
            "Tool Use output": tool_output,
            "Proximity output": proximity_output,
            "Reflection outputs": reflection_bundle,
            "Ranking output": ranking_output,
            "Meta-review output": meta_output,
            "Evolution output": evolution_output,
            "PI final feedback": pi_feedback,
        }
        text = ["# Cycle Summary"]
        for title, content in sections.items():
            text.extend(["", f"## {title}", content.strip()])
        (cycle_dir / "cycle_summary.md").write_text("\n".join(text).strip() + "\n", encoding="utf-8")
