"""Tests for support agent multi-turn routing."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from agent.run_agent import run_multi_turn  # noqa: E402


def test_cancel_uses_order_from_history():
    result = run_multi_turn(
        {
            "user_message": "Can you cancel it?",
            "history": [
                {"role": "user", "content": "What's the status of my order?"},
                {
                    "role": "assistant",
                    "content": "Your order #1234 has been shipped and should arrive in 2 days.",
                },
            ],
            "turn_index": 1,
        }
    )
    tools = [step["tool"] for step in result["trace"] if step["type"] == "tool_call"]
    assert tools == ["cancel_order"]
    assert "#1234" in result["final_output"]
