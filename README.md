# README - To-Do List API

Este é um guia passo a passo para configurar, executar e solucionar problemas do projeto To-Do List API , que utiliza Supabase como banco de dados, Docker para containerização e Python com FastAPI como backend.

## Requisitos

1. Python 3.11+
2. Docker e Docker Compose
3. Supabase (conta ativa e projeto criado)

## Estrutura do Projeto

to-do-list/
├── src/
│   ├── main.py                # Ponto de entrada da aplicação
│   ├── todolist/              # Módulo contendo rotas e lógica da API
│   │   ├── router/            # Rotas da API
│   │   └── schemas.py         # Definição dos modelos Pydantic
│   └── shared/                # Configuração compartilhada (ex.: banco de dados)
│       └── database.py        # Configuração do SQLAlchemy
├── Dockerfile                 # Arquivo para construir a imagem Docker
├── docker-compose.yml         # Configuração do Docker Compose
├── requirements.txt           # Dependências do Python
├── .env                       # Variáveis de ambiente
└── .gitignore                 # Arquivos ignorados pelo Git

## Configuração Inicial

1. Instale as Dependências Locais
   Certifique-se de que todas as dependências estão instaladas no seu ambiente local:
   ``pip install -r requirements.txt``
2. Configure o .env
   Crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis:
   DATABASE_URL=postgresql://postgres:[YOUR_PASSWORD]@[DB_HOST]:[PORT]/postgres

## Execução do Projeto

1. Execute Localmente (Sem Docker)
   Se você deseja executar o projeto localmente (sem Docker), use o seguinte comando:
   ``uvicorn src.main:app --reload``
2. Execute com Docker
   Para executar o projeto usando Docker:
   Construa e inicie os contêineres:
   ``docker-compose up --build``
   A API estará disponível em http://localhost:8000/docs
3. Teste no banco de dados
   Execute uma consulta simples no Supabase para verificar se o banco de dados está funcionando:
   ``SELECT * FROM todos LIMIT 1;``

## Próximos Passos

1. Implementação de autenticação: Adicionar autenticação JWT para proteger os endpoints.
2. Documentação Swagger: Configurar a documentação automática usando Swagger UI.

Licença
Este projeto está licenciado sob a MIT License . Consulte o arquivo LICENSE para mais detalhes.
