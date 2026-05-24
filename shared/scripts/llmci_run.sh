#!/usr/bin/env bash
# Run llmci with an alternate config file (until llmci CLI supports --config).
set -euo pipefail

CONFIG="llmci.yaml"
EXTRA=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --config)
      CONFIG="$2"
      shift 2
      ;;
    *)
      EXTRA+=("$1")
      shift
      ;;
  esac
done

RESTORE=0
CREATED=0
if [[ "$CONFIG" != "llmci.yaml" ]]; then
  if [[ -f llmci.yaml ]]; then
    cp llmci.yaml .llmci.yaml.bak
    RESTORE=1
  else
    CREATED=1
  fi
  cp "$CONFIG" llmci.yaml
fi

set +e
if ((${#EXTRA[@]})); then
  llmci run "${EXTRA[@]}"
else
  llmci run
fi
STATUS=$?
set -e

if [[ "$RESTORE" -eq 1 ]]; then
  mv .llmci.yaml.bak llmci.yaml
elif [[ "$CREATED" -eq 1 ]]; then
  rm -f llmci.yaml
fi

exit $STATUS
