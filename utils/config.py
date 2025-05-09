# utils/config.py

import pendulum
import os
from dotenv import load_dotenv

# Carrega variáveis do .env assim que o módulo for importado
load_dotenv()

# Data de início padrão com timezone UTC (boas práticas no Airflow)
DEFAULT_START_DATE = pendulum.datetime(2024, 6, 30, tz="UTC")

# Argumentos padrão para tarefas em DAGs
DEFAULT_ARGS = {
    "retries": 1,
    "retry_delay": pendulum.duration(seconds=10),
}

# Nome do aluno lido do ambiente — útil em mensagens genéricas
NOME_ALUNO = os.getenv("NOME_ALUNO", "aluno desconhecido")

# Tag padrão para marcar DAGs de aula
TAG_AULA = "aula"
