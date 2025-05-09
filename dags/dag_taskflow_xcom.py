# dags/dag_taskflow_xcom.py

# Importa decoradores modernos do Airflow para criar DAGs e tasks com Python puro
from airflow.decorators import dag, task
import pendulum


# Define a DAG com decorador, utilizando boas práticas de timezone e catchup
@dag(
    dag_id="dag_taskflow_xcom",                        # Nome da DAG
    start_date=pendulum.datetime(2024, 6, 30, tz="UTC"),  # Data de início
    schedule_interval=None,                            # Execução manual
    catchup=False,                                     # Não executa execuções passadas
    tags=["aula", "taskflow", "xcom"]                  # Tags visuais na UI
)
def fluxo_com_xcom():
    """
    DAG de exemplo usando a TaskFlow API.
    Mostra como passar dados entre tasks automaticamente via XCom.
    """

    @task
    def gerar_nome():
        """
        Task 1 – Simula a geração de um nome (exemplo: entrada de um sistema externo).
        Retorna o nome, que será passado automaticamente para a próxima task.
        """
        return "Lucas"

    @task
    def exibir_nome(nome_recebido):
        """
        Task 2 – Recebe o nome da task anterior e imprime a mensagem.
        O valor é passado automaticamente via XCom.
        """
        print(f"O nome recebido via XCom foi: {nome_recebido}")

    # Encadeamento: a saída de gerar_nome é passada como argumento para exibir_nome
    nome = gerar_nome()
    exibir_nome(nome)


# Executa a DAG quando o Airflow a interpretar
fluxo_com_xcom()
