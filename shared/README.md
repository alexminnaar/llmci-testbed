# Shared utilities

Cross-service helpers for the Acme Support testbed.

- `mock_llm.py` — deterministic LLM stub when `MOCK_LLM=1`
- `scripts/wait_for_http.sh` — curl loop for CI service startup
- `scripts/llmci_run.sh` — run evals with alternate config files (`--config`)
