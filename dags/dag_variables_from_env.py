# dags/dag_variables_from_env.py

# Importa as classes principais do Airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum

# 🛠️ Importa a função utilitária para obter o nome do aluno via variável de ambiente
# Como a pasta `utils` foi movida para dentro de `dags`, usamos o prefixo `dags.`
from utils.env import get_nome_aluno


def imprimir_mensagem():
    """
    Função chamada pela task.
    Lê o nome do aluno do .env e imprime uma saudação personalizada.
    """
    nome = get_nome_aluno()
    print(f"Olá, {nome}! Essa DAG está lendo o valor diretamente do arquivo .env.")


# Define argumentos padrão para a DAG (ex: retry em caso de falha)
default_args = {
    "retries": 1,
    "retry_delay": pendulum.duration(seconds=10),
}

# Cria a DAG em si
with DAG(
    dag_id="dag_variables_from_env",  # Nome visível na interface do Airflow
    start_date=pendulum.datetime(2024, 6, 30, tz="UTC"),  # Data de início com fuso UTC
    schedule_interval=None,           # Execução apenas manual
    catchup=False,                    # Não executa DAGs passadas
    default_args=default_args,
    tags=["aula", "env", "dotenv"]    # Tags para facilitar busca na UI
) as dag:

    # Criação da task que imprime a mensagem
    saudacao = PythonOperator(
        task_id="saudacao_env",
        python_callable=imprimir_mensagem,
    )
