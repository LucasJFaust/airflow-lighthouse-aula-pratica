# Super README | Aula Prática de Apache Airflow com Docker Compose e Astro CLI

Este projeto foi desenvolvido como material de apoio para a aula **"Apache Airflow | Aula Prática"** do programa Lighthouse. O objetivo é ensinar, na prática, como estruturar, executar, configurar e testar DAGs no Apache Airflow utilizando Docker Compose e, posteriormente, o Astro CLI.

> **Importante:** A aula parte do pressuposto de que os alunos já tiveram uma introdução teórica ao Airflow e à orquestração de dados. Por isso, aqui focamos 100% na prática.

---

## ✨ Visão Geral

Este repositório está organizado com base nas boas práticas de engenharia de dados e ensino. As DAGs foram desenvolvidas de forma incremental, com o objetivo de evoluir o aprendizado a cada exemplo. Cada DAG tem um propósito didático específico.

## 📚 Ferramentas e Tecnologias Utilizadas

| Ferramenta         | Função                                                           |
| ------------------ | ---------------------------------------------------------------- |
| **Apache Airflow** | Orquestração de workflows de dados.                              |
| **Docker Compose** | Ambiente padronizado para execução do Airflow.                   |
| **Makefile**       | Automatiza comandos do Docker Compose para facilitar a execução. |
| **Poetry**         | Gerenciamento de dependências do projeto Python.                 |
| **pipx**           | Instala ferramentas CLI Python de forma isolada.                 |
| **pyenv**          | Gerencia múltiplas versões do Python em paralelo.                |
| **Astro CLI**      | Interface da Astronomer para executar e testar DAGs localmente.  |

### ⚠️ Observação
As ferramentas para genrenciamento de versões e controle de ambientes virtuais (pyenv, pipx e poetry) **NÃO** são obrigátórias para reprodução do projeto. Vocês podem estar usando a que for mais confortável para vocês.
---

## 🌐 Requisitos de Ambiente

Para reproduzir este projeto, siga esta ordem de instalação e configuração no seu ambiente local (de preferência via WSL no Windows ou Linux/macOS). Mais instruções vão estar listada posteriormente neste documento:

### 1. Instalação do `pyenv`

Permite alternar entre múltiplas versões do Python. Instalamos, por exemplo, o Python 3.11.8 com:

```bash
curl https://pyenv.run | bash
# Adicione as configurações ao seu shell (bash/zsh)
# Reinicie o terminal após isso
pyenv install 3.11.8
pyenv global 3.11.8
```

### 2. Instalação do `pipx`

Facilita a instalação de CLIs Python sem poluir o ambiente global:

```bash
python -m pip install --user pipx
pipx ensurepath
```

Feche e reabra o terminal ou execute `source ~/.bashrc` ou `source ~/.zshrc`.

### 3. Instalação do `poetry`

Gerencia o ambiente virtual e dependências do projeto:

```bash
pipx install poetry
```

Configure o poetry para criar os ambientes virtuais dentro do diretório do projeto:

```bash
poetry config virtualenvs.in-project true
```

### 4. Instalar o Astro CLI

Usado para testar DAGs localmente em ambientes compatíveis com o Astronomer:

```bash
curl -sSL https://install.astronomer.io | sudo sh
```

Verifique a instalação com:

```bash
astro version
```

---

## 🚀 Iniciando o Projeto com Poetry

### ✅ Passo 1 – Criar o diretório do projeto

```bash
mkdir airflow-lighthouse-aula-pratica
cd airflow-lighthouse-aula-pratica
```

### ✅ Passo 2 – Inicializar o projeto com o Poetry

```bash
poetry init
```

Siga as instruções do terminal e escolha `n` para todas as dependências por enquanto (vamos instalar depois manualmente).

### ✅ Passo 3 – Ativar a versão do Python desejada com o pyenv

Certifique-se de estar usando o Python correto:

```bash
pyenv local 3.11.8
```

Esse comando cria um arquivo `.python-version` no projeto. Isso garante que o Poetry vai usar a versão correta ao criar o ambiente virtual.

### ✅ Passo 4 – Criar o ambiente virtual

```bash
poetry install
```

O Poetry vai criar o ambiente virtual em `.venv/` e instalar as dependências do `pyproject.toml` (inicialmente vazio, mas será preenchido ao longo do projeto).

> 💡 **Dica:** Sempre ative o ambiente virtual antes de rodar qualquer coisa:

```bash
poetry shell
```

### ✅ Passo 5 – Instalar dependências principais do projeto

```bash
poetry add apache-airflow requests
```

---

## 🚧 Estrutura do Projeto (Docker Compose)

```
.
├── .git/ # Diretório de versionamento Git
├── .venv/ # Ambiente virtual Python
├── dags/ # Contém todas as definições das DAGs do Airflow
│ ├── pycache/ # Cache de módulos Python
│ ├── utils/ # Módulos de utilidades e configurações para as DAGs
│ │ ├── pycache/
│ │ ├── init.py
│ │ ├── config.py # Configurações gerais
│ │ ├── env.py # Variáveis de ambiente
│ │ └── messages.py # Mensagens ou textos para as DAGs
│ ├── 1-dag_variables_operator.py # Exemplo de DAG utilizando Airflow Variables via operador
│ ├── 2-dag_variables_via_ui.py # Exemplo de DAG obtendo variáveis via UI
│ ├── 3-dag_variables_from_env.py # Exemplo de DAG lendo variáveis de ambiente
│ ├── 4-dag_config_example.py # Exemplo de DAG com configuração externa
│ ├── 5-dag_pipeline_simples.py # DAG que demonstra um pipeline de dados simples
│ ├── 6-dag_docker_operator_example.py # DAG usando DockerOperator
│ └── 7-dag_taskflow_xcom.py # DAG com TaskFlow API e XComs
├── infra/ # Definições de infraestrutura (Docker Compose)
│ └── docker-compose.yml # Arquivo para orquestrar serviços Docker
├── logs/ # Diretório para logs de execução do Airflow e DAGs
│ ├── dag_id=dag_docker_operator_example/
│ ├── dag_id=dag_pipeline_simples/
│ ├── dag_processor_manager/
│ └── scheduler/
├── output/ # Diretório para dados de saída gerados pelas DAGs
│ └── estados_ibge.csv # Exemplo de arquivo de saída
├── .env # Arquivo para variáveis de ambiente locais
├── .gitignore # Regras para ignorar arquivos no Git
├── .python-version # Define a versão do Python (usado pelo pyenv)
├── logs.sh # Script para visualizar logs dos contêineres
├── Makefile # Orquestrador de comandos de build e execução
├── poetry.lock # Gerenciamento de dependências com Poetry
├── pyproject.toml # Configuração do projeto e dependências com Poetry
├── README.md # Este arquivo de documentação
├── reset.sh # Script para resetar o ambiente Airflow
├── start.sh # Script para iniciar o ambiente Airflow
└── stop.sh # Script para parar o ambiente Airflow

```
### ⚠️ Observação
As pastas logs e output não vão estar no repositório pois estão no gitignore.
---
## 🧩 DAG 1: 1_dag_variables_operator.py

### 🎯 Objetivo

Introduzir o conceito de DAG no Airflow e mostrar como utilizar o operador PythonOperator com funções Python simples.

### 🔍 O que essa DAG faz?

Ela lê uma variável de ambiente (via Airflow Variables) e imprime o conteúdo usando uma task com PythonOperator. Foi feita para apresentar:

* O uso do @dag e @task
* A estrutura mínima de uma DAG
* Como fazer um log no Airflow com context['ti'].xcom_push
* Como recuperar variáveis da interface do Airflow

### 💡 Conceitos abordados

* Criação básica de DAG
* Uso de PythonOperator
* Airflow Variables
* Logging no Airflow

### ✅ Boas práticas utilizadas

* Uso de logs estruturados
* Separação clara entre definição da DAG e lógica de negócio
* Nomeação intuitiva da DAG e das tasks

---
## 🧩 DAG 2: `2_dag_variables_via_ui.py`

### 🌟 Objetivo

Demonstrar como utilizar as **Airflow Variables** de maneira mais prática, definindo seus valores diretamente pela interface Web do Airflow (Web UI), em vez de hardcoded no código Python.

Essa DAG tem o propósito de mostrar para os alunos uma maneira mais flexível e recomendada de parametrizar o comportamento de DAGs em produção.

### 🔍 O que essa DAG faz?

Essa DAG lê o valor de uma variável chamada `mensagem_ui` definida diretamente no menu "Admin > Variables" da interface do Airflow, e imprime seu conteúdo no log. Para isso, ela utiliza o `PythonOperator` chamando uma função que acessa a variável com `Variable.get()`.

### 📊 Conceitos abordados

* Utilização de Airflow Variables via Web UI
* Como recuperar valores de variáveis usando `Variable.get()`
* Separar a parametrização da lógica de execução
* Boas práticas para tornar o código mais reutilizável e amigável para alterações futuras

### ✅ Boas práticas utilizadas

* Uso de variáveis externas para configurar comportamento
* A DAG falha com erro explicativo caso a variável não exista, incentivando validação
* Comentários explicativos no código
* Criação de uma única task simples com foco em clareza

### ⚠️ Observação

Essa DAG só funcionará corretamente caso a variável `mensagem_ui` tenha sido previamente criada via UI do Airflow. Caso contrário, uma exceção será levantada durante a execução da task. Isso reforça a importância da configuração correta do ambiente antes de rodar a DAG.

---
## 🧩 DAG 3: `3_dag_variables_from_env.py`

### 🎯 Objetivo

Mostrar como tornar as DAGs mais portáveis e seguras ao ler variáveis diretamente de um arquivo `.env`, sem depender da configuração manual na interface do Airflow. Isso permite controle por versionamento e facilita a reprodução em diferentes ambientes.

### 🔍 O que essa DAG faz?

Essa DAG é uma evolução da anterior. Ela:

* Usa o pacote `python-dotenv` para ler variáveis de ambiente de um arquivo `.env` localizado na raiz do projeto;
* Recupera essas variáveis diretamente no código Python usando `os.getenv()`;
* Faz logs das variáveis lidas.

### 📂 Arquivos criados/modificados

* `.env`: Criado na raiz do projeto contendo as variáveis necessárias.
* `3_dag_variables_from_env.py`: Contém a DAG que consome essas variáveis.

Exemplo do `.env`:

```dotenv
NOME=Lucas
IDADE=30
```

### ✅ Dependência adicionada ao projeto

Adicionamos ao projeto o pacote `python-dotenv` via Poetry:

```bash
poetry add python-dotenv
```

### 💡 Conceitos abordados

* Isolamento de configuração por ambiente
* Uso de `.env` em projetos Python
* Uso de `os.getenv()`

### ✅ Boas práticas utilizadas

* **Segurança**: evita salvar informações sensíveis diretamente no código.
* **Portabilidade**: facilita a execução da DAG em qualquer ambiente com o mesmo `.env`.
* **Organização**: separa variáveis de execução do código-fonte.

---
## 🧩 DAG 4: `4_dag_config_example.py`

### 🎯 Objetivo

Demonstrar como centralizar parâmetros e configurações da DAG em um módulo separado (`config.py`). Isso promove organização e reutilização, além de facilitar a manutenção.

### 🔍 O que essa DAG faz?

Essa DAG é uma evolução da DAG anterior. Ela utiliza um arquivo `config.py` dentro da pasta `utils/` para centralizar informações como:

* ID da DAG
* Descrição
* Data de início (start\_date)
* Intervalo de agendamento (schedule\_interval)

A DAG em si é simples e tem apenas uma task que imprime uma mensagem, mas seu foco está na melhoria de arquitetura.

### 🧱 Componentes do Projeto Utilizados

* `dags/4_dag_config_example.py`: a DAG principal, agora com importações vindas de `utils/config.py`.
* `dags/utils/config.py`: arquivo com variáveis de configuração da DAG.

### ✅ Boas práticas utilizadas

* **Centralização de configurações**: evita hardcoded e facilita alterações futuras.
* **Separação de responsabilidades**: o arquivo `config.py` contém apenas configurações, enquanto a DAG contém a lógica.
* **Reutilização de parâmetros**: os valores definidos no `config.py` podem ser usados em múltiplas DAGs.

### 📁 Estrutura dos arquivos relacionados

```
├── dags/
│   ├── 4_dag_config_example.py
│   └── utils/
│       └── config.py
```

### 💡 Conceitos abordados

* Organização de projetos Airflow
* Separação entre configuração e código
* Evolução incremental de DAGs

### 📌 Observação

Essa DAG não apresenta funcionalidades novas em termos de execução ou operadores, mas é um excelente exemplo de melhoria arquitetural. Essa refatoração será útil para DAGs maiores e mais complexas ao longo do projeto.

## 🧩 DAG 5: `5_dag_pipeline_simples.py`

### 🎯 Objetivo

Demonstrar uma pipeline simples de dados orquestrada pelo Airflow, com múltiplas tarefas encadeadas. Essa DAG busca ilustrar um fluxo realista de ETL (Extract, Transform, Load), utilizando operadores básicos e boas práticas.

### 🔍 O que essa DAG faz?

Essa DAG realiza o seguinte fluxo de trabalho:

1. **Extração de dados da API do IBGE**: Faz uma requisição HTTP e salva os dados de estados brasileiros em CSV.
2. **Transformação dos dados**: Lê o CSV, transforma o conteúdo (por exemplo, filtrando ou formatando os dados).
3. **Carregamento**: Simula o carregamento dos dados transformados em algum destino (ex: banco ou storage).

Todos esses passos foram implementados com `PythonOperator`, de forma simples e didática.

### 💡 Conceitos abordados

* Criação de múltiplas `PythonOperator` encadeadas
* Logging em cada etapa do pipeline
* Manipulação de arquivos CSV em Python
* Encadeamento de tarefas com `.set_downstream()` ou via decorator (dependendo da versão)

### ✅ Boas práticas utilizadas

* Separação clara das responsabilidades de cada etapa do pipeline
* Utilização de logs para rastreabilidade
* Nomeação descritiva para DAGs e tasks
* Código comentado para fins didáticos

### 🛠️ Outras observações

* O arquivo CSV é salvo no diretório `output/`, que foi montado via volume no Docker.
* O código utiliza a biblioteca `requests` para comunicação com a API pública do IBGE.
* Essa DAG é um ótimo ponto de partida para mostrar como uma DAG pode representar um pipeline real e ser facilmente expandida.

---
## 🧩 DAG 6: `6_dag_docker_operator_example.py`

### 🌟 Objetivo

Apresentar como o Apache Airflow pode executar tarefas dentro de containers Docker utilizando o `DockerOperator`. Este exemplo é essencial para demonstrar como integrar workflows do Airflow com ambientes isolados e reproduzíveis, que é uma prática comum em pipelines de dados modernas.

### 🔍 O que essa DAG faz?

Esta DAG executa um container Docker que roda um script Python simples, localizado na pasta `include/hello-world.py`. O script apenas imprime uma mensagem no terminal, simulando uma tarefa de processamento isolada.

### ⚖️ Por que usamos o `DockerOperator`?

* Para garantir isolamento de ambiente.
* Para facilitar a portabilidade e reprodutibilidade.
* Para executar códigos que dependem de bibliotecas específicas sem interferir no ambiente principal do Airflow.

### 📝 Etapas realizadas

1. Criei o script `include/hello-world.py` que contém um print simples:

   ```python
   print("Hello from Docker!")
   ```

2. Configurei o caminho do volume que será montado no container, permitindo que o Airflow acesse o script.

3. Utilizei o `DockerOperator` para executar o container com a imagem `python:3.11-slim`.

4. Montei o volume da pasta `include/` para dentro do container em `/app`, e executei:

   ```bash
   python /app/hello-world.py
   ```

### 💡 Boas Práticas Adotadas

* Utiliza imagens leves (como `python:3.11-slim`).
* Define o volume com `Mount` de forma explícita, garantindo controle de acesso aos arquivos.
* Define `auto_remove=True` para que o container seja removido após a execução.
* Usa nomes descritivos para tasks e DAG.

### ⚠️ Pontos de Atenção

* O Docker precisa estar funcionando corretamente no host (e acessível pelo Airflow).
* É necessário garantir que o path local montado esteja correto e com permissão adequada.
* Containers com `auto_remove=False` podem acumular lixo se não forem limpos.

### 🌐 Relacionamento com o Mundo Real

* Esse tipo de DAG é comum em pipelines que executam scripts legados, modelos de machine learning ou qualquer código que tenha dependências específicas.
* Também é muito usada para rodar transformações pesadas que precisam de ambientes dedicados.

---
## 🧩 DAG 7: `7_dag_taskflow_xcom.py`

### 🌟 Objetivo

Apresentar o uso do decorator `@task` do TaskFlow API do Airflow e demonstrar como as tasks podem se comunicar entre si usando XComs de forma implícita (sem necessidade de `xcom_push` e `xcom_pull`).

Essa é uma das formas mais modernas e legíveis de se construir DAGs em Airflow.

---

### 🔍 O que essa DAG faz?

* Extraí uma lista de nomes de estados do Brasil (dados simulados ou importados de forma simples);
* Transforma os nomes (por exemplo, colocando todos em maiúsculas);
* Salva os resultados em um arquivo `.csv` dentro da pasta `output/`.

---

### 🔧 Ferramentas utilizadas

* `@dag` e `@task` (TaskFlow API)
* Manipulação de listas em Python
* Escrita de arquivos `.csv`

---

### ✅ Boas práticas utilizadas

* Nomeação clara de tasks
* Uso da TaskFlow API para facilitar o compartilhamento de dados via retorno de funções
* Modularização das etapas: `extrair`, `transformar`, `salvar`
* Organização da saída em uma pasta dedicada `output/`

---

### 🎓 Conceitos didáticos ensinados

* O que é o TaskFlow API
* Como usar `@task` e `@dag`
* Como ocorre a troca de dados entre tasks com retorno de funções (XCom implícito)
* Benefícios dessa abordagem sobre o uso explícito de XComs
* Escrita e leitura de arquivos com Python dentro de DAGs

---

### 🔗 Conexão com as aulas anteriores

Esta é uma evolução natural das primeiras DAGs, pois apresenta uma abordagem mais moderna e robusta, preparando o terreno para workflows mais complexos e reutilizáveis.

Ao usar o TaskFlow, a legibilidade aumenta e o risco de erros com XComs manuais diminui.

## 📁 Infraestrutura e Execução do Projeto com Docker Compose

Esta seção detalha todos os arquivos auxiliares criados para facilitar a execução e o gerenciamento do projeto. Inclui explicações do `docker-compose.yml`, scripts `.sh`, `Makefile`, organização dos diretórios e como tudo isso interage para que os alunos possam reproduzir 100% do ambiente.

---

### 📂 `infra/docker-compose.yml`

Este é o principal arquivo que define a infraestrutura do ambiente de orquestração. Ele:

* Usa a imagem oficial do Astronomer Runtime (baseada em Apache Airflow)
* Define os volumes para montar DAGs, logs, plugins, e a pasta de output
* Mapeia as portas para acesso via navegador (Webserver)

Trecho importante:

```yaml
dags:
  - ./dags:/usr/local/airflow/dags
```

Isso garante que qualquer DAG escrita localmente estará visível dentro do container do Airflow.

Outros pontos relevantes:

* `output/` também é montado, pois é onde salvamos dados extraídos
* Os logs da execução ficam em `logs/`
* Plugins customizados estariam em `plugins/`, mesmo que não tenhamos usado aqui

---

### 🔹 Estrutura de diretórios

```bash
.
├── dags/                  # Contém as DAGs e o módulo utils/
│   ├── utils/             # Funções auxiliares reutilizáveis (como leitura de variáveis e logs)
├── logs/                  # Logs gerados pela execução do Airflow
├── output/                # Arquivos de saída gerados pelas DAGs
├── infra/                 # Contém o docker-compose.yml
├── start.sh, stop.sh, reset.sh, logs.sh  # Scripts auxiliares
├── Makefile               # Alternativa centralizada para os scripts
```

---

## Scripts de Gerenciamento do Ambiente

Para simplificar a interação com o ambiente Docker do Apache Airflow e otimizar as tarefas do dia a dia, este projeto utiliza uma série de scripts shell (`.sh`). Eles abstraem comandos complexos do Docker e do Airflow CLI, tornando o processo de inicialização, parada e monitoramento muito mais intuitivo.

**Importante:** Antes de executar qualquer script `.sh` pela primeira vez, certifique-se de que ele tenha permissões de execução. Você pode conceder essas permissões usando o comando `chmod +x nome_do_script.sh` no terminal.

A seguir, a descrição e o modo de uso de cada script:

### 1. `start.sh` - Iniciando o Ambiente Airflow

*   **Função:** Este script é o ponto de entrada para levantar todo o seu ambiente Apache Airflow, incluindo os serviços de Webserver, Scheduler, Worker, banco de dados (Postgres) e Redis, todos dentro de contêineres Docker. Ele também garante que o banco de metadados do Airflow seja inicializado e um usuário administrador seja criado, se ainda não existirem.
*   **Quando usar:** Sempre que você precisar iniciar o ambiente Airflow do zero ou reiniciá-lo após uma parada.
*   **Como usar:**
    ```bash
    ./start.sh
    ```
*   **Detalhes:** Ele executa os comandos `docker compose up -d` (para iniciar os serviços em segundo plano) e `docker compose exec airflow-webserver airflow db upgrade`, `airflow users create`, entre outros, para configurar o Airflow.

### 2. `stop.sh` - Parando o Ambiente Airflow

*   **Função:** Este script é responsável por parar todos os serviços do Airflow que estão rodando em contêineres Docker. Ele desliga os contêineres de forma controlada.
*   **Quando usar:** Quando você terminar de trabalhar no projeto e quiser liberar os recursos do seu computador, ou antes de realizar alterações profundas no ambiente.
*   **Como usar:**
    ```bash
    ./stop.sh
    ```
*   **Detalhes:** Ele executa o comando `docker compose down`, que para e remove os contêineres, mas mantém os volumes de dados para persistência.

### 3. `reset.sh` - Resetando o Ambiente Airflow (Com Cuidado!)

*   **Função:** Este é um script de "limpeza total". Ele não apenas para os serviços do Airflow, mas também remove *todos* os volumes de dados associados ao projeto (incluindo o banco de dados do Airflow). Isso significa que você perderá o histórico de execução de DAGs, logs antigos e configurações de usuários.
*   **Quando usar:** **Use com extrema cautela!** É ideal para quando você quer começar completamente do zero, como se tivesse acabado de clonar o repositório, ou para resolver problemas persistentes com o banco de dados do Airflow. Na maioria dos casos, `stop.sh` e `start.sh` são suficientes.
*   **Como usar:**
    ```bash
    ./reset.sh
    ```
*   **Detalhes:** Ele executa `docker compose down -v --remove-orphans`, garantindo uma limpeza profunda.

### 4. `logs.sh` - Visualizando os Logs do Ambiente

*   **Função:** Este script permite visualizar os logs de todos os serviços do Airflow rodando em contêineres Docker em tempo real. É essencial para depuração e monitoramento do que está acontecendo no seu ambiente.
*   **Quando usar:** Sempre que precisar diagnosticar um problema, verificar se os serviços estão iniciando corretamente ou acompanhar a execução de tasks.
*   **Como usar:**
    ```bash
    ./logs.sh
    ```
*   **Detalhes:** Ele executa `docker compose logs -f`, mostrando a saída de log de todos os contêineres e acompanhando novas linhas (modo "follow"). Pressione `Ctrl+C` para sair da visualização de logs.

---

### 🚀 Outra Opção para Execução (Makefile)

1. Ative o ambiente virtual com `poetry shell`
2. Inicie os containers:

```bash
make start
# ou
bash start.sh
```

3. Acesse o Airflow em `http://localhost:8080` com:

* **Login:** airflow
* **Senha:** airflow

4. Execute a DAG desejada na interface ou aguarde o agendamento

5. Veja os arquivos gerados na pasta `output/`

6. Acompanhe os logs com:

```bash
./logs.sh
```

---