#!/usr/bin/env python3
"""Mock API that returns JSON responses."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def handle_request(input_text: str) -> str:
    if "user_id=123" in input_text and "orders" not in input_text.lower():
        return json.dumps({"user_id": 123, "name": "Alice", "email": "alice@example.com"})
    if "user_id=456" in input_text:
        return json.dumps({"user_id": 456, "name": "Bob", "email": "bob@example.com"})
    if "customer_id=123" in input_text:
        return json.dumps({"customer_id": 123, "orders": [{"id": 1, "total": 29.99}]})
    if "sku=ABC-100" in input_text:
        return json.dumps({"sku": "ABC-100", "name": "Widget", "price": 9.99, "in_stock": True})
    if "name=Charlie" in input_text:
        return json.dumps({"results": [{"user_id": 789, "name": "Charlie"}], "count": 1})
    return json.dumps({"error": "Unknown request"})


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    data = json.loads(Path(args.input).read_text())
    result = handle_request(data["input"])
    Path(args.output).write_text(json.dumps({"output": result}))


if __name__ == "__main__":
    main()
