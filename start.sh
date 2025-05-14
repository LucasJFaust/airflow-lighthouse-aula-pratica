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

# 3. Mensagem final ao usuário com informações de acesso
echo "---"
echo "Airflow iniciado com sucesso!"
echo "Acesse a interface em: http://localhost:8080"
echo "Login: airflow | Senha: airflow"
echo "---"
