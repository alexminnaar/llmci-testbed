# Scaffold Testbed — Acme Support

[![Scaffold Evals](https://github.com/alexminnaar/scaffold-testbed/actions/workflows/scaffold.yml/badge.svg)](https://github.com/alexminnaar/scaffold-testbed/actions/workflows/scaffold.yml)

Realistic customer monorepo for dogfooding [Scaffold](https://github.com/alexminnaar/scaffold) ([`llmci`](https://pypi.org/project/llmci/) on PyPI). Fictional company **Acme Support** runs ticket classification, RAG helpdesk, summarization QA, and a support agent — all evaluable with `scaffold run`.

**Implementation spec:** [TESTBED_OUTLINE.md](https://github.com/alexminnaar/scaffold/blob/main/TESTBED_OUTLINE.md) in the main Scaffold repo.

## Prerequisites

- Python 3.11+
- [`llmci`](https://pypi.org/project/llmci/) from PyPI

```bash
make install
# or: pip install -e ".[dev]"
```

CI runs `pip install --upgrade llmci` so new PyPI releases are picked up automatically.

**Scaffold developers only** — unreleased CLI changes:

```bash
pip install "llmci @ git+https://github.com/alexminnaar/scaffold@main"
```

## Quick start

```bash
make install
make eval-classifier
```

## Alternate config files

The `llmci` CLI does not yet support `scaffold run --config`. Use the wrapper from each service directory:

```bash
MOCK_LLM=1 ../../shared/scripts/scaffold_run.sh --config scaffold-prompt.yaml
```

## Services

| Service | Path | Docs case study | Scaffold example |
|---------|------|-----------------|------------------|
| Ticket classifier | `services/ticket-classifier/` | FastAPI Service | `examples/08-fastapi-service` |
| RAG QA | `services/rag-qa/` | RAG Pipeline | `examples/07-pipeline-level` |
| Summarizer | `services/summarizer/` | Summarization QA | `examples/09-summarization-qa` |
| Support agent | `services/support-agent/` | Support Agent | `examples/05`, `06` |
| JSON API | `services/json-api/` | Custom judge | `examples/04-custom-judge` |
| Model migration | `migration/` | Multi-Model Migration | `examples/02-model-migration` |

## Mock vs real LLM

| Variable | Default (CI) | Purpose |
|----------|--------------|---------|
| `MOCK_LLM` | `1` | Deterministic keyword/fixture logic |
| `OPENAI_API_KEY` | unset | Required for real LLM judge / migration |

CI runs all services in mock mode with `--compare-to=origin/main` on PRs. Use **Scaffold LLM Evals** (manual dispatch) for real LLM runs.

## Run all mock evals

```bash
make eval-all
```

Covers the same 7 eval configs as the CI matrix.

## HTTP testing (ticket classifier)

```bash
docker compose up -d
../../shared/scripts/wait_for_http.sh http://localhost:8000/health
cd services/ticket-classifier
CLASSIFIER_URL=http://localhost:8000 MOCK_LLM=1 scaffold run
```

## Add a new service

1. Create `services/<name>/` with `scaffold.yaml`, `evals/*.jsonl`, and a command target script.
2. Add a matrix entry to `.github/workflows/scaffold.yml`.
3. On `main`: `MOCK_LLM=1 scaffold run --update-baseline` and commit `.scaffold/baselines/`.

## Links

- [Scaffold on GitHub](https://github.com/alexminnaar/scaffold)
- [llmci on PyPI](https://pypi.org/project/llmci/)

## Demo regression branches

Open PRs from these branches to see Scaffold fail CI and post a PR comment:

| Branch | Change | Expected failure |
|--------|--------|------------------|
| `test/break-classifier` | Remove billing keywords | `service-classification` accuracy |
| `test/break-rag-retrieval` | Force empty retrieval | `rag-qa` pass_rate |
| `test/break-agent-safety` | Agent calls `delete_account` on normal queries | `support-agent-single` mean_score |

```bash
git checkout -b test/break-classifier
# edit services/ticket-classifier/app/classifier.py
git push -u origin test/break-classifier
```
