#!/bin/bash

RUNNER_DIR="/home/nsee/actions-runner(QEMULA)"

# Verifica se o runner já está rodando
if pgrep -f "run.sh" > /dev/null; then
    echo "O Runner já está rodando!"
    exit 0
fi

# Inicia o Runner
cd "$RUNNER_DIR" || exit
./run.sh
