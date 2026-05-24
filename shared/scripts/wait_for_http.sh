#!/usr/bin/env bash
set -euo pipefail

URL="${1:-http://localhost:8000/health}"
MAX_ATTEMPTS="${2:-30}"
SLEEP_SECONDS="${3:-2}"

for attempt in $(seq 1 "$MAX_ATTEMPTS"); do
  if curl -sf "$URL" >/dev/null; then
    echo "Service ready: $URL"
    exit 0
  fi
  echo "Waiting for $URL (attempt $attempt/$MAX_ATTEMPTS)..."
  sleep "$SLEEP_SECONDS"
done

echo "Timed out waiting for $URL" >&2
exit 1
