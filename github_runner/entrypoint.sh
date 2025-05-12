#!/bin/bash
set -e

./config.sh \
  --url "${REPO_URL}" \
  --token "${RUNNER_TOKEN}" \
  --name docker-runner \
  --work _work \
  --unattended \
  --replace

echo "Iniciando runner..."
exec ./run.sh
