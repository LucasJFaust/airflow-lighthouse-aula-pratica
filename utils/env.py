# utils/env.py

# Importamos load_dotenv para carregar variáveis do arquivo .env
from dotenv import load_dotenv

# Importamos os para acessar as variáveis via os.getenv()
import os

# Carrega as variáveis do arquivo .env assim que o módulo for importado
load_dotenv()

def get_nome_aluno():
    """
    Recupera a variável de ambiente NOME_ALUNO.
    Se não estiver definida, retorna 'aluno desconhecido' como padrão.
    """
    return os.getenv("NOME_ALUNO", "aluno desconhecido")
