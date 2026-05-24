"""Mock answer generation from retrieved context."""

from __future__ import annotations


def generate(query: str, context: list[str]) -> str:
    if not context:
        return "I don't have enough information to answer that question."

    combined_context = " ".join(context)
    query_lower = query.lower()
    if "what is" in query_lower or "explain" in query_lower:
        return f"Based on the documentation: {combined_context}"
    if "how" in query_lower:
        return f"Here's how: {combined_context}"
    return f"Answer: {combined_context}"
