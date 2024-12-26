#!/bin/bash

# Caminho do arquivo de lista de repositórios
REPO_FILE="ListaDeRepos/repos.txt"

# Diretório base para armazenar os subtrees
DEST_DIR="outros"

# Verifica se o arquivo existe
if [ ! -f "$REPO_FILE" ]; then
    echo "Arquivo $REPO_FILE não encontrado!"
    exit 1
fi

# Cria o diretório base se não existir
mkdir -p "$DEST_DIR"

# Lê cada linha do arquivo
while read -r REPO_URL; do
    # Ignora linhas vazias
    if [ -z "$REPO_URL" ]; then
        continue
    fi

    # Extrai o nome do repositório
    REPO_NAME=$(basename -s .git "$REPO_URL")

    echo "Adicionando $REPO_NAME..."

    # Adiciona o repositório como subtree
    git subtree add --prefix="$DEST_DIR/$REPO_NAME" "$REPO_URL" HEAD || {
        echo "Erro ao adicionar $REPO_NAME. Verifique o repositório."
        continue
    }

    echo "$REPO_NAME adicionado com sucesso!"
done < "$REPO_FILE"

echo "Todos os repositórios foram processados!"
