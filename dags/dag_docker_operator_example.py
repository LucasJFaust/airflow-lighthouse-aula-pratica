# dags/dag_docker_operator_example.py

"""
DAG de exemplo usando o DockerOperator
Executa um contêiner Docker que imprime uma mensagem no terminal
"""

from airflow.decorators import dag  # Importa o decorador para criar DAGs
from airflow.providers.docker.operators.docker import DockerOperator  # Operador que roda containers
from datetime import timedelta
import pendulum

# Define os parâmetros padrão para a DAG (retries, delay, etc.)
default_args = {
    "retries": 1,
    "retry_delay": timedelta(seconds=10),
}

# Define a DAG usando o decorador
@dag(
    dag_id="dag_docker_operator_example",  # Nome visível na UI do Airflow
    start_date=pendulum.datetime(2024, 6, 30, tz="UTC"),  # Data inicial com timezone UTC
    schedule_interval=None,  # Execução apenas manual
    catchup=False,
    default_args=default_args,
    tags=["aula", "docker", "operator"],  # Tags ajudam a organizar na interface
)
def docker_operator_dag():
    """
    DAG que executa um contêiner com Alpine Linux para imprimir uma mensagem.
    Demonstra o uso do DockerOperator no Airflow. Escolhi o Alpine por ser uma imagem leve e rápida.
    O comando executado dentro do contêiner é um simples echo, mas poderia ser qualquer outro comando.
    O operador DockerOperator é útil para executar tarefas que dependem de ambientes isolados ou específicos,
    como processamento de dados, execução de scripts, ou qualquer tarefa que possa ser encapsulada em um contêiner.
    O uso do DockerOperator permite que você mantenha a portabilidade e a reprodutibilidade das suas tarefas,
    além de facilitar o gerenciamento de dependências e versões de software.
    """

    # Define a task com DockerOperator
    executar_container = DockerOperator(
        task_id="exemplo_docker_operator",
        image="alpine:latest",                 # Imagem Docker que será executada
        command='echo "Rodando container via DockerOperator!"',  # Comando que será executado dentro do contêiner
        auto_remove=True,                      # Remove o contêiner após a execução
        docker_url="unix://var/run/docker.sock",  # URL do daemon Docker (configuração padrão no host)
        network_mode="bridge",                 # Usa o modo de rede padrão
    )

    # Como só temos uma task, não há necessidade de encadeamento
    executar_container


# Instancia a DAG para que o Airflow a reconheça
docker_operator_dag()
