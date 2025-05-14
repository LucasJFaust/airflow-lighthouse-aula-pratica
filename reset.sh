#!/bin/bash

# Script para resetar completamente o ambiente Airflow com Docker Compose
# CUIDADO: isso remove todos os dados, incluindo o volume do banco de dados

# Caminho do arquivo docker-compose
COMPOSE_FILE=infra/docker-compose.yml

# Aviso ao usuário
echo "⚠️  Atenção: este comando irá remover todos os dados persistentes do ambiente Airflow!"
echo "Isso inclui o banco de dados (PostgreSQL) e arquivos gerados nos volumes."

# Solicita confirmação do usuário
read -p "Tem certeza que deseja continuar? [s/N]: " confirm

# Verifica a resposta do usuário
if [[ "$confirm" == "s" || "$confirm" == "S" ]]; then
  # Executa o down com -v para remover volumes (dados do banco, logs, etc.)
  echo "Encerrando e limpando os contêineres e volumes..."
  docker compose -f $COMPOSE_FILE down -v

  echo "Ambiente resetado com sucesso."
else
  echo "Operação cancelada. Nenhuma alteração foi feita."
fi

