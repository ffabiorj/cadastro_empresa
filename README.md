[![Build Status](https://travis-ci.com/ffabiorj/cadastro_empresa.svg?branch=master)](https://travis-ci.com/ffabiorj/voluntario_app)

[![codecov](https://codecov.io/gh/ffabiorj/cadastro_empresa/branch/master/graph/badge.svg)](https://codecov.io/gh/ffabiorj/voluntario_app)

# Criação de um app de cadastro de empresas.

## Link do projeto e da api em produção.

[App em produção](https://cadastro-empresa.herokuapp.com/)

[Api em produção](https://cadastro-empresa.herokuapp.com/api/v1/empresas/)

## Ferramentas

- Django
- Postgres
- Heroku
- Django restframework

## Roda o projeto localmente:

1. Clone o repositório.
2. Entre na pasta.
3. Crie uma um ambiente de desenvolvimento com python 3.8.
4. Ative o ambiente.
5. Instale as dependências.
6. Crie um arquivo .env
7. Rode as migrações
8. Rode o projeto
9. Acesse o link

```
- git clone git@github.com:ffabiorj/cadastro_empresa.git
- cd cadastro_empresa
- python3 -m venv .venv
- source .venv/bin/activate
- pip install -r requirements-dev.txt
- python contrib/env_gen.py
- python manage.py migrate
- python manage.py runserver
- http://127.0.0.1:8000/
```

### Endpoints da api

- http://127.0.0.1:8000/api/v1/empresas/ # retorna todos os emprestimos do usuario
- http://127.0.0.1:8000/api/v1/empresas/id/ # retorna um emprestimo pelo id

### Exemplos de entrada para os endpoints

```
Dados para cadastrar empresa na api
{
    "razao_social": "teste",
    "nome_fantasia": "teste",
    "cnpj": "35.379.838/0001-12",
    "email": "fabio20rj@gmail.com",
    "endereco": "nereu sampaio, 61",
    "cidade": "Rio de Janeiro",
    "estado": "MG",
    "telefone": "(21)3333-3333",
    "data_cadastro": "2020-12-10",
    "status": "A",
    "risco": "C",
    "agencia": "333-3",
    "conta": "33.333-3",
}

```

### Rodar os testes

```

pytest

```

### Links para as ferramentas utilizadas

[Django](https://docs.djangoproject.com/)

[Postgres](https://www.postgresql.org/)

[Heroku](https://www.heroku.com/)

[Codecov](https://codecov.io/)

[Travis](https://travis-ci.com/)

[Django Rest Framework](https://www.django-rest-framework.org/)
