#!/usr/bin/env python3
"""Summarization command wrapper."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from summarizer import summarize  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    data = json.loads(Path(args.input).read_text())
    result = summarize(data["input"])
    Path(args.output).write_text(json.dumps({"output": result}))


if __name__ == "__main__":
    main()
