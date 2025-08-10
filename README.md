# Inicializando Projeto

## Libs

- **UV**: Escolhida como gerenciador de pacotes do projeto. Vai servir para garantir o versionamento das dependências bem como criar ambientes com versões específicas para que estas não interfiram com de outros projetos. Referência: https://docs.astral.sh/uv 

- **FastAPI**: lib que vai ser utilizada para facilitar a criação de API. Referência: https://fastapi.tiangolo.com/#requirements

## Rodando o Projeto

- **Inicializar**: [bash] fastapi dev main.py;
- **URL**: [url]  http://127.0.0.1:8000;
- **Corrigir erros de formatação**: [bash] uv run ruff format;
- **Ler Documentação da API**: [url]  http://127.0.0.1:8000/docs