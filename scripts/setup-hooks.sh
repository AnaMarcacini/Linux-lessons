#!/bin/bash

# Caminho para o diretório de hooks do Git
HOOKS_DIR=".git/hooks"

# Caminho para o diretório onde estão os hooks (dentro de scripts/hooks)
HOOKS_SOURCE_DIR="scripts/hooks"

# Verifica se o diretório de hooks existe
if [ -d "$HOOKS_SOURCE_DIR" ]; then
    # Copia os hooks do diretório 'scripts/hooks' para '.git/hooks'
    cp "$HOOKS_SOURCE_DIR"/* "$HOOKS_DIR/"
    echo "Hooks instalados com sucesso!"
else
    echo "Diretório 'scripts/hooks' não encontrado!"
fi
