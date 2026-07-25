from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Protocol

from .config import PROMPT_FILES, read_required_text
from .deepseek_client import ChatResult


class ChatClient(Protocol):
    def complete(
        self,
        messages: list[dict[str, str]],
        *,
        model: str | None = None,
        temperature: float = 0.2,
        max_tokens: int | None = None,
    ) -> ChatResult:
        ...


@dataclass(frozen=True)
class AgentSpec:
    key: str
    name: str
    prompt_key: str
    temperature: float = 0.2
    max_tokens: int | None = None
    system_note: str = ""


class AgentRunner:
    def __init__(self, root: Path, client: ChatClient, model: str) -> None:
        self.root = root
        self.client = client
        self.model = model
        self.prompt_cache: dict[str, str] = {}

    def prompt(self, prompt_key: str) -> str:
        if prompt_key not in PROMPT_FILES:
            raise KeyError(f"Unknown prompt key: {prompt_key}")
        if prompt_key not in self.prompt_cache:
            self.prompt_cache[prompt_key] = read_required_text(self.root, PROMPT_FILES[prompt_key])
        return self.prompt_cache[prompt_key]

    def run(self, spec: AgentSpec, user_message: str, output_path: Path) -> str:
        system_prompt = self.prompt(spec.prompt_key)
        if spec.system_note:
            system_prompt = f"{system_prompt}\n\nAdditional role instruction:\n{spec.system_note}"
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ]
        result = self.client.complete(
            messages,
            model=self.model,
            temperature=spec.temperature,
            max_tokens=spec.max_tokens,
        )
        output_path.parent.mkdir(parents=True, exist_ok=True)
        content = result.content.strip()
        output_path.write_text(content + "\n", encoding="utf-8")
        self._write_response_metadata(spec, output_path, result, content)
        return content

    def _write_response_metadata(
        self,
        spec: AgentSpec,
        output_path: Path,
        result: ChatResult,
        content: str,
    ) -> None:
        choice = result.raw.get("choices", [{}])[0] if isinstance(result.raw.get("choices"), list) else {}
        metadata = {
            "agent_key": spec.key,
            "prompt_key": spec.prompt_key,
            "configured_model": self.model,
            "response_model": result.raw.get("model") or result.raw.get("_codex_request_model"),
            "request_model": result.raw.get("_codex_request_model"),
            "thinking": result.raw.get("_codex_thinking"),
            "finish_reason": choice.get("finish_reason") if isinstance(choice, dict) else None,
            "usage": result.raw.get("usage"),
            "content_chars": len(content),
        }
        meta_path = output_path.with_suffix(output_path.suffix + ".meta.json")
        meta_path.write_text(json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8")
