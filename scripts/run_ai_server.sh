#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
cd "$ROOT_DIR"

if [ ! -d .venv ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate

pip install -r ai_engine/requirements.txt

export PYTHONPATH=$ROOT_DIR
exec uvicorn ai_engine.server.main:app --host ${AI_SERVICE_HOST:-0.0.0.0} --port ${AI_SERVICE_PORT:-8001} --reload
