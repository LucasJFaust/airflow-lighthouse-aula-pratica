#!/bin/bash

# Script para parar os serviços do Airflow sem apagar volumes ou dados
# Útil quando você quer apenas interromper a execução temporariamente

# Caminho do arquivo docker-compose
COMPOSE_FILE=infra/docker-compose.yml

echo "Parando os serviços do Airflow..."
docker compose -f $COMPOSE_FILE down

echo "Serviços encerrados com sucesso."
