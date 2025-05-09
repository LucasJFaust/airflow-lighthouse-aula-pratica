# dags/dag_variables_via_ui.py

from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum

# Importa a função que monta a mensagem a partir de uma variável do Airflow
from utils.messages import mensagem_airflow_ui


def imprimir_mensagem_ui():
    """
    Função executada pela task.
    Imprime uma saudação lida a partir das Airflow Variables.
    """
    print(mensagem_airflow_ui())


default_args = {
    "retries": 1,
    "retry_delay": pendulum.duration(seconds=10),
}

with DAG(
    dag_id="dag_variables_via_ui",
    start_date=pendulum.datetime(2024, 6, 30, tz="UTC"),
    schedule_interval=None,
    catchup=False,
    default_args=default_args,
    tags=["aula", "variaveis", "airflow-ui"]
) as dag:

    task = PythonOperator(
        task_id="saudacao_airflow_ui",
        python_callable=imprimir_mensagem_ui,
    )
