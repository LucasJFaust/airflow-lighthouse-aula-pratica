# dags/dag_config_example.py

from airflow import DAG
from airflow.operators.python import PythonOperator

# Importa os parâmetros centralizados do projeto (aqui mudamos o caminho para usar o docker compose)
from dags.utils.config import DEFAULT_START_DATE, DEFAULT_ARGS, NOME_ALUNO, TAG_AULA


def saudacao_configurada():
    """
    Função usada pela task.
    Utiliza a variável NOME_ALUNO definida no config.py para imprimir uma mensagem.
    """
    print(f"Olá, {NOME_ALUNO}! Esta DAG usa parâmetros centralizados via config.py.")


# Criação da DAG com uso dos parâmetros importados
with DAG(
    dag_id="dag_config_example",          # Nome visível na UI
    start_date=DEFAULT_START_DATE,        # Usando data padrão do config
    schedule_interval=None,               # Execução manual
    catchup=False,
    default_args=DEFAULT_ARGS,            # Retry e delays vindos do config
    tags=[TAG_AULA, "config"]             # Tags vindas do config
) as dag:

    # Task que imprime a mensagem
    task = PythonOperator(
        task_id="saudacao_configurada",
        python_callable=saudacao_configurada,
    )
