#!/usr/bin/env bash
# Run scaffold with an alternate config file (until scaffold CLI supports --config).
set -euo pipefail

CONFIG="scaffold.yaml"
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
if [[ "$CONFIG" != "scaffold.yaml" ]]; then
  if [[ -f scaffold.yaml ]]; then
    cp scaffold.yaml .scaffold.yaml.bak
    RESTORE=1
  else
    CREATED=1
  fi
  cp "$CONFIG" scaffold.yaml
fi

set +e
if ((${#EXTRA[@]})); then
  scaffold run "${EXTRA[@]}"
else
  scaffold run
fi
STATUS=$?
set -e

if [[ "$RESTORE" -eq 1 ]]; then
  mv .scaffold.yaml.bak scaffold.yaml
elif [[ "$CREATED" -eq 1 ]]; then
  rm -f scaffold.yaml
fi

exit $STATUS
