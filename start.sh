#!/bin/bash

# Script para iniciar o ambiente Airflow via Docker Compose
# Crei ele para reproduzir o projeto localmente de forma padronizada

# 1. Inicializa o banco de dados do Airflow (apenas na primeira vez ou quando resetar)
echo "Inicializando o banco de dados do Airflow..."
docker compose up airflow-init

# 2. Sobe todos os serviços do ambiente Airflow em segundo plano (modo -d = detached para não bloquear o terminal)
echo "Subindo todos os serviços do Airflow..."
docker compose up -d

# 3. Mensagem final ao usuário
echo "---"
echo "Airflow iniciado com sucesso!"
echo "Acesse a interface em: http://localhost:8080"
echo "Login: airflow | Senha: airflow"
echo "---"
