#!/bin/bash

# Script para iniciar o ambiente Airflow via Docker Compose
# Atualizado para garantir a ordem correta de execução
# e evitar problemas de inicialização do banco de dados

# Caminho relativo do arquivo docker-compose.yml
COMPOSE_FILE=infra/docker-compose.yml

# 1. Inicializa o banco de dados do Airflow
# Usa o comando 'run' em vez de 'up' para executar e remover o container de inicialização automaticamente (--rm)
# Isso evita que o terminal fique bloqueado e garante que o processo termine corretamente
echo "Inicializando o banco de dados do Airflow..."
docker compose -f $COMPOSE_FILE run --rm airflow-init

# 2. Sobe os serviços principais do Airflow em segundo plano
# O parâmetro '-d' (detached) garante que o terminal fique livre após o comando
echo "Subindo todos os serviços do Airflow..."
docker compose -f $COMPOSE_FILE up -d airflow-webserver airflow-scheduler airflow-db

# 3. Aguarda alguns segundos para garantir que o webserver esteja inicializado
# (Podemos melhorar no futuro com uma checagem ativa via curl ou healthcheck)
echo "Aguardando o Airflow Webserver inicializar..."
sleep 15

# 4. Cria o usuário admin padrão para login na interface
# Se o usuário já existir, o comando falha silenciosamente com uma mensagem de aviso
echo "Criando usuário admin padrão (se ainda não existir)..."
docker exec airflow_webserver airflow users create \
  --username airflow \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email airflow@example.com \
  --password airflow || echo "⚠️  Usuário já existe. Pulando criação."

# 5. Mensagem final ao usuário com informações de acesso
echo "---"
echo "✅ Airflow iniciado com sucesso!"
echo "🌐 Acesse a interface em: http://localhost:8080"
echo "🔐 Login: airflow | Senha: airflow"
echo "---"
