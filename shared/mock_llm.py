"""Deterministic LLM stub for mock CI runs."""

from __future__ import annotations

import os


def is_mock() -> bool:
    return os.environ.get("MOCK_LLM", "0") == "1"


def complete(prompt: str, *, model: str = "mock") -> str:
    """Return deterministic text from prompt keywords when MOCK_LLM=1."""
    if not is_mock():
        import litellm

        response = litellm.completion(model=model, messages=[{"role": "user", "content": prompt}])
        return response.choices[0].message.content.strip()

    prompt_lower = prompt.lower()

    category_keywords = {
        "hardware": ["printer", "monitor", "keyboard", "webcam", "hardware"],
        "billing": ["refund", "charged", "invoice", "subscription", "billing"],
        "account": ["password", "login", "account", "two-factor"],
        "software": ["crash", "app", "bug", "software", "error"],
    }
    for category, keywords in category_keywords.items():
        if any(kw in prompt_lower for kw in keywords):
            return category

    if "summarize" in prompt_lower or "summary" in prompt_lower:
        lines = [line.strip() for line in prompt.splitlines() if line.strip()]
        content_lines = [line for line in lines if not line.startswith(("Summarize", "Article:", "Ticket:"))]
        if content_lines:
            return content_lines[0][:200]
        return "Summary unavailable."

    return "general"
