# Importação da classe DAG (estrutura principal do airflow)
from airflow import DAG

# Importação do operador que vai nos permitir rodar funções Python como tasks
from airflow.operators.python import PythonOperator

# Importação do operador que vai nos permitir acessar variáveis definidas na UI do airflow
from airflow.models import Variable

# Importação padrão para definir data de início e intervalos de retry
# Aqui optei pelo pendulum pois ele lida nativamente com as timezones
import pendulum

# Esta é a função Python que será executada pela task
# Ela busca uma variável chamada "nome_aluno" na interface do Airflow
# e imprime uma mensagem personalizada
def hello_from_variable():
    # Tenta buscar a variável "nome_aluno" (criada em Admin > Variables)
    # Se não existir, usa "aluno desconhecido" como valor padrão
    nome = Variable.get("nome_aluno", default_var="aluno desconhecido")

    # Imprime a mensagem no log da task
    print(f"Olá, {nome}! Essa é sua primeira DAG com AIrflow")


# # Parâmetros padrão aplicados a todas as tasks da DAG (caso não sejam sobrescritos)
default_args = {
    "retries": 1, # Se a task falhar, o Airflow tenta mais uma vez
    "retry_delay": pendulum.duration(seconds=10), # Espera 10s antes de tentar de novo
}

# Define a data de início da DAG usando pendulum com fuso UTC (boa prática recomendada)
start = pendulum.datetime(2024, 6, 30, tz="UTC")

# Criação da DAG em si, usando a sintaxe com o geranciador de contexto "with" para agrupar as tasks
with DAG(
    dag_id="dag_variables_operator",    # Nome único da DAG na interface do Airflow
    start_date=start,                   # Quando o Airflow pode começar a agendar essa DAG
    schedule_interval=None,             # Definimos como "manual", sem agendamento automático
    catchup=False,                      # Não executa DAGs do passado se estiver inativa por um tempo
    default_args=default_args,          # Aplica os parâmetro padrões que definimos anteriormente
    tags=["aula", "variaveis"]          # Tags visuais para organizar na UI
) as dag:

    # Criação da task que executa a função hello_from_variable
    task_1 = PythonOperator(
        task_id= "exibe_mensagem",      # Nome da task na UI
        python_callable=hello_from_variable,  # Função que será executada quando a task rodar
    )