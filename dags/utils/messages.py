# utils/messages.py

from airflow.models import Variable

def mensagem_airflow_ui():
    """
    Recupera a variável 'nome_aluno' definida na interface do Airflow (Admin > Variables).
    Caso a variável não esteja definida, retorna 'aluno desconhecido'.
    """
    nome = Variable.get("nome_aluno", default_var="aluno desconhecido")
    return f"Olá, {nome}! Esta mensagem foi carregada a partir de uma Airflow Variable."
