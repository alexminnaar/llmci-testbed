"""Smoke tests for shared utilities."""

from shared.mock_llm import complete, is_mock


def test_is_mock_default(monkeypatch):
    monkeypatch.delenv("MOCK_LLM", raising=False)
    assert is_mock() is False

    monkeypatch.setenv("MOCK_LLM", "1")
    assert is_mock() is True


def test_complete_mock_billing(monkeypatch):
    monkeypatch.setenv("MOCK_LLM", "1")
    result = complete("Ticket: I was charged twice for my subscription", model="mock")
    assert result == "billing"
