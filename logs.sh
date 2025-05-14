#!/bin/bash

# Script para visualizar os logs em tempo real do serviço webserver do Airflow
# Ajuda a depurar problemas e verificar se o servidor web está rodando corretamente

# Caminho do arquivo docker-compose
COMPOSE_FILE=infra/docker-compose.yml

echo "Exibindo os logs em tempo real do Airflow Webserver..."
docker compose -f $COMPOSE_FILE logs -f airflow-webserver
