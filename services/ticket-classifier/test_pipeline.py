"""Smoke tests for ticket classifier pipeline."""

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT.parent.parent))

from app.pipeline import classify, preprocess  # noqa: E402


@pytest.fixture(autouse=True)
def mock_mode(monkeypatch):
    monkeypatch.setenv("MOCK_LLM", "1")


def test_pii_redaction():
    text = "Call me at 555-123-4567 or email alice@example.com"
    cleaned = preprocess(text)
    assert "[PHONE]" in cleaned
    assert "[EMAIL]" in cleaned


def test_classify_billing():
    result = classify("I was charged twice for my subscription renewal")
    assert result["category"] == "billing"
