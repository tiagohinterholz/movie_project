# Movie Project

Este é um projeto Django para gerenciar filmes, usuários e listas de favoritos, utilizando a API do The Movie Database (TMDB).

O projeto é containerizado com Docker para facilitar a configuração e execução do ambiente de desenvolvimento.

## Tecnologias Utilizadas

Este projeto foi construído utilizando um conjunto de tecnologias modernas para desenvolvimento web e APIs.

- **Backend:**
    - **Python 3.12**: Linguagem de programação principal.
    - **Django 5.2**: Framework web robusto para o desenvolvimento rápido e seguro.
    - **Django REST Framework**: Toolkit poderoso para a construção de APIs Web.
    - **Gunicorn**: Servidor WSGI para deploy em produção.

- **Banco de Dados:**
    - **PostgreSQL 16**: Sistema de gerenciamento de banco de dados relacional.
    - **Psycopg2**: Adaptador de banco de dados PostgreSQL para Python.

- **Autenticação:**
    - **Simple JWT (djangoframework-simplejwt)**: Implementação de autenticação baseada em JSON Web Token.

- **Containerização:**
    - **Docker**: Plataforma para desenvolver, enviar e executar aplicações em containers.
    - **Docker Compose**: Ferramenta para definir и executar aplicações Docker multi-container.

- **Testes:**
    - **Pytest**: Framework de testes para escrever testes simples e escaláveis.
    - **Pytest-Django**: Plugin para integrar o Pytest com o Django.
    - **Faker**: Biblioteca para gerar dados falsos para os testes.

- **Outras Ferramentas:**
    - **Django CORS Headers**: Para lidar com Cross-Origin Resource Sharing (CORS).
    - **python-dotenv**: Para gerenciar variáveis de ambiente a partir de um arquivo `.env`.
    - **DRF Spectacular**: Para gerar documentação de API (Swagger/OpenAPI).

## Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Como Executar a Aplicação

O projeto é configurado para ser executado com um único comando.

1.  **Clone o repositório:**
    ```bash
    git clone <url-do-seu-repositorio>
    cd movie_project
    ```

2.  **Suba os containers:**
    Execute o comando abaixo na raiz do projeto:
    ```bash
    docker-compose up --build
    ```
    - O argumento `--build` garante que a imagem Docker da aplicação será construída (ou reconstruída se houver alterações).
    - Este comando irá iniciar dois serviços: `db` (banco de dados PostgreSQL) e `web` (a aplicação Django).

### O que acontece automaticamente?

Ao iniciar os containers, o script de entrada (`entrypoint.sh`) cuidará de tudo para você:
- **Criação do `.env`**: Se o arquivo `.env` não existir, um novo será criado com as configurações padrão para o ambiente local.
- **Migrações do Banco de Dados**: O script aguarda o banco de dados ficar pronto e aplica as migrações do Django (`python manage.py migrate`).
- **Criação do Superusuário**: Um superusuário padrão será criado se não existir:
    - **Usuário:** `admin`
    - **Senha:** `admin123`

## Acessando a Aplicação

- **API Django**: A aplicação estará disponível em [http://localhost:8000/](http://localhost:8000/).
- **Admin Django**: Você pode acessar a área administrativa em [http://localhost:8000/admin/](http://localhost:8000/admin/) e fazer login com as credenciais do superusuário.

## Executando Testes

Para rodar a suíte de testes, utilize o seguinte comando com os containers em execução:

```bash
docker-compose exec movies_backend pytest
```

Este comando executa o `pytest` dentro do container da aplicação (`movies_backend`).

## Parando a Aplicação

Para parar os containers, pressione `Ctrl + C` no terminal onde o `docker-compose up` está rodando, ou execute o seguinte comando em outro terminal:

```bash
docker-compose down
```
