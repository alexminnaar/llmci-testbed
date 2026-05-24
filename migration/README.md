# Model Migration

Demonstrates `llmci migrate` on ticket classification prompt.

## Usage

```bash
export OPENAI_API_KEY=...
llmci migrate \
  --from openai/gpt-4o \
  --to openai/gpt-4o-mini \
  --eval ticket-classification \
  --patience 3 \
  --max-iterations 10
```

## Expected holdout score

After migration, expect holdout accuracy in the **0.85–0.95** range with `gpt-4o-mini` on the ticket dataset.

Excluded from default PR CI (requires API key). Run via **llmci LLM Evals** workflow or locally.

Maps to docs case study `cs-migration` and `examples/02-model-migration`.
