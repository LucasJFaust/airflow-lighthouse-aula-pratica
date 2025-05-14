# Makefile com comandos úteis para iniciar, parar e resetar o ambiente Airflow
# Utiliza a flag -f para apontar diretamente para o arquivo docker-compose.yml

COMPOSE_FILE=infra/docker-compose.yml

# Inicia os serviços do Airflow em modo background (detached)
up:
	docker compose -f $(COMPOSE_FILE) up -d

# Inicializa o banco de dados do Airflow (primeira vez ou após reset)
init:
	docker compose -f $(COMPOSE_FILE) up airflow-init

# Para os contêineres sem remover volumes
stop:
	docker compose -f $(COMPOSE_FILE) down

# Remove todos os dados persistentes (banco, logs, volumes)
reset:
	docker compose -f $(COMPOSE_FILE) down -v

# Exibe os logs do webserver em tempo real
logs:
	docker compose -f $(COMPOSE_FILE) logs -f airflow-webserver
