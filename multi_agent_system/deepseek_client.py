from __future__ import annotations

from dataclasses import dataclass
import json
import time
from typing import Any
from urllib import error, request


class DeepSeekError(RuntimeError):
    pass


@dataclass(frozen=True)
class ChatResult:
    content: str
    raw: dict[str, Any]


class DeepSeekClient:
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.deepseek.com",
        model: str = "deepseek-v4-pro",
        fallback_model: str | None = "deepseek-v4-flash",
        thinking: str = "enabled",
        reasoning_effort: str | None = None,
        timeout_seconds: int = 120,
        max_tokens: int = 4096,
        retries: int = 2,
    ) -> None:
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.fallback_model = fallback_model
        self.thinking = thinking
        self.reasoning_effort = reasoning_effort
        self.timeout_seconds = timeout_seconds
        self.max_tokens = max_tokens
        self.retries = retries

    @property
    def chat_url(self) -> str:
        if self.base_url.endswith("/chat/completions"):
            return self.base_url
        return f"{self.base_url}/chat/completions"

    def complete(
        self,
        messages: list[dict[str, str]],
        *,
        model: str | None = None,
        temperature: float = 0.2,
        max_tokens: int | None = None,
    ) -> ChatResult:
        primary_model = model or self.model
        model_attempts = [primary_model]
        if self.fallback_model and self.fallback_model != primary_model:
            model_attempts.append(self.fallback_model)
        last_error: Exception | None = None
        for current_model in model_attempts:
            payload = {
                "model": current_model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens or self.max_tokens,
                "thinking": {"type": self.thinking},
            }
            if self.thinking == "enabled" and self.reasoning_effort:
                payload["reasoning_effort"] = self.reasoning_effort
            data = json.dumps(payload).encode("utf-8")
            for attempt in range(self.retries + 1):
                try:
                    req = request.Request(
                        self.chat_url,
                        data=data,
                        method="POST",
                        headers={
                            "Authorization": f"Bearer {self.api_key}",
                            "Content-Type": "application/json",
                            "Accept": "application/json",
                        },
                    )
                    with request.urlopen(req, timeout=self.timeout_seconds) as response:
                        raw = json.loads(response.read().decode("utf-8"))
                    content = raw["choices"][0]["message"].get("content") or ""
                    raw.setdefault("_codex_request_model", current_model)
                    raw.setdefault("_codex_thinking", self.thinking)
                    if content.strip():
                        return ChatResult(content=content, raw=raw)
                    last_error = DeepSeekError(f"DeepSeek returned empty content for model {current_model}")
                except error.HTTPError as exc:
                    body = exc.read().decode("utf-8", errors="replace")
                    last_error = DeepSeekError(f"DeepSeek HTTP {exc.code}: {body[:1200]}")
                except Exception as exc:  # noqa: BLE001 - preserve upstream network context.
                    last_error = exc
                if attempt < self.retries:
                    time.sleep(1.5 * (attempt + 1))

        raise DeepSeekError(f"DeepSeek request failed: {last_error}") from last_error


class DryRunClient:
    def __init__(self, model: str = "dry-run") -> None:
        self.model = model

    def complete(
        self,
        messages: list[dict[str, str]],
        *,
        model: str | None = None,
        temperature: float = 0.2,
        max_tokens: int | None = None,
    ) -> ChatResult:
        del temperature, max_tokens
        system = messages[0]["content"] if messages else ""
        user = messages[-1]["content"] if messages else ""
        content = (
            f"[DRY RUN RESPONSE]\n"
            f"Model: {model or self.model}\n"
            f"System prompt chars: {len(system)}\n"
            f"User message chars: {len(user)}\n\n"
            f"System prompt preview:\n{system[:600]}\n\n"
            f"User message preview:\n{user[:1200]}\n"
        )
        return ChatResult(content=content, raw={"dry_run": True})
