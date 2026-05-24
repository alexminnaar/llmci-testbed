"""Heuristic judge for deterministic CI summarizer evals."""

from __future__ import annotations

import re


def _content_words(text: str) -> set[str]:
    words = re.findall(r"[a-z0-9]+", text.lower())
    stopwords = {"the", "a", "an", "is", "are", "was", "were", "in", "on", "at", "to", "for", "of", "and"}
    return {w for w in words if w not in stopwords and len(w) > 2}


def evaluate(input: str, expected: str, actual: str) -> dict:
    if not expected:
        source_words = _content_words(input)
        actual_words = _content_words(actual)
        if not actual_words:
            return {"score": 0.0, "reason": "empty summary"}
        overlap = len(source_words & actual_words) / len(actual_words)
        score = 1.0 if overlap >= 0.5 else 0.5 if overlap >= 0.3 else 0.0
        return {"score": score, "reason": f"source overlap {overlap:.2f}"}

    expected_words = _content_words(expected)
    actual_words = _content_words(actual)
    if not expected_words:
        return {"score": 1.0}

    found = len(expected_words & actual_words) / len(expected_words)
    score = 1.0 if found >= 0.6 else 0.5 if found >= 0.35 else 0.0
    return {"score": score, "reason": f"{found:.0%} reference word overlap"}
