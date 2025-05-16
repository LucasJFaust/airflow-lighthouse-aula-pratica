# DAG: dag_pipeline_simples.py
# Objetivo: Extrair dados da API do IBGE, transformar e salvar em CSV usando boas práticas

# Importa os decoradores modernos do Airflow para criar DAGs e tasks com Python puro
from airflow.decorators import dag, task

# Pendulum é usado em vez de datetime porque é timezone-aware (recomendado pelo Airflow)
import pendulum

# Tive que importar timedelta do módulo datetime para usar no retry
from datetime import timedelta

# Requests é usado para fazer requisições HTTP à API do IBGE
import requests

# CSV é usado para salvar os dados em formato legível em disco
import csv

# Path é usado para manipular caminhos de arquivo de forma robusta e multiplataforma
from pathlib import Path

# Define o diretório onde o CSV final será salvo
# Usa Path para garantir compatibilidade com Windows/Linux/Mac
OUTPUT_PATH = Path(__file__).parents[1] / "output"
OUTPUT_PATH.mkdir(exist_ok=True)  # Cria o diretório se ele não existir

@dag(
    dag_id="dag_pipeline_simples",  # Nome da DAG visível na UI
    start_date=pendulum.datetime(2024, 6, 30, tz="UTC"),  # Data de início com timezone correto
    schedule_interval=None,  # Não agenda automaticamente, só executa manual
    catchup=False,  # Evita execuções retroativas
    tags=["aula", "etl", "ibge"]  # Ajuda a categorizar a DAG na UI
)
def pipeline_ibge():
    """
    DAG que simula um pipeline ETL simples:
    - Extrai dados da API do IBGE
    - Transforma para extrair campos de interesse
    - Salva os dados transformados como CSV local
    """

    @task(retries=3, retry_delay=timedelta(seconds=10))
    def extrair_dados():
        """
        Extrai a lista de estados brasileiros da API do IBGE.
        Inclui retry em caso de falhas na rede.
        """
        url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
        response = requests.get(url, timeout=10)  # Limita tempo de espera da API

        if response.status_code != 200:
            raise Exception(f"Erro na requisição: {response.status_code}")

        estados = response.json()  # Converte JSON em lista de dicionários Python
        return estados  # Retorno automático via XCom para a próxima task

    @task()
    def transformar_dados(estados):
        """
        Recebe os dados brutos da API e filtra os campos:
        - id
        - nome
        - sigla
        - nome da região
        """
        dados_transformados = []

        for estado in estados:
            dados_transformados.append({
                "id": estado["id"],
                "nome": estado["nome"],
                "sigla": estado["sigla"],
                "regiao": estado["regiao"]["nome"]
            })

        return dados_transformados  # Retorna para a próxima etapa via XCom

    @task()
    def salvar_dados(dados):
        """
        Salva os dados em formato CSV local dentro da pasta output/
        """
        caminho_arquivo = OUTPUT_PATH / "estados_ibge.csv"

        # Abre o arquivo em modo escrita, com codificação UTF-8 e sem quebra de linha extra
        with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "nome", "sigla", "regiao"])
            writer.writeheader()  # Escreve o cabeçalho do CSV
            writer.writerows(dados)  # Escreve todas as linhas

        print(f"CSV gerado com sucesso: {caminho_arquivo}")  # Log na interface do Airflow

    # Encadeia as tasks: extração → transformação → carregamento
    estados_brutos = extrair_dados()
    estados_transformados = transformar_dados(estados_brutos)
    salvar_dados(estados_transformados)

# Garante que a DAG seja reconhecida pelo Airflow ao interpretar este arquivo
pipeline_ibge()
