"""Semicolon-separated fact judge for RAG QA."""

from __future__ import annotations


def evaluate(input: str, expected: str, actual: str) -> dict:
    facts = [f.strip() for f in expected.split(";") if f.strip()]
    found = sum(1 for fact in facts if fact.lower() in actual.lower())
    score = found / len(facts) if facts else 1.0
    return {"score": score, "reason": f"{found}/{len(facts)} facts found"}
