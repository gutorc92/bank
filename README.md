# Bank

O projeto visa a construção e simulação de uma api bancária.

## Instalação

### Banco de dados

Para criar o banco de dados utilize o gerenciador de container docker na pasta raiz. 

```bash
docker-compose up
```

### Ambiente python

Use o gerenciador [pip](https://pip.pypa.io/en/stable/) para instalar o gerenciador de pacotes
pipenv.

```bash
pip install pipenv
```

Dentro da pasta bank-api instale os pacotes necessários para rodar o projeto.

```bash
pipenv install
```

Para criar as tabelas do banco de dados use o comando:

```bash
flask db upgrade
```

Para rodar o projeto:

```bash
export FLASK_ENV=development
flask run
```

Acesse a rota para verificar se tudo correu como o planejado:

```http://localhost:5000```



#### Testes

```bash
pytest
```