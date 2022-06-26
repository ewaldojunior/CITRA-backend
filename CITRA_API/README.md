
# CITRA - backend
## PIES II


#### Pré-requisitos e como rodar a aplicação:

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python](https://www.python.org). 
Além disto, é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/).
Lembrando que, o banco de dados utilizado é o [PostgreSQL](https://www.postgresql.org/)

#### 🎲 Rodando a aplicação:

```bash
# Clone este repositório
$ git clone https://github.com/ewaldojunior/CITRA-backend

# Acesse a pasta do projeto no terminal/cmd
$ cd CITRA-backend

# Instale o ambiente virtual
$ python -m venv .venv

# Entre no ambiente virtual
$ source .venv/Scripts/activate

# Instale as bibliotecas necessárias do requirements.txt
$ pip install -r requirements.txt

# Entre no ambiente virtual
$ cd CITRA-API/

# Execute a aplicação em modo de desenvolvimento
$ python manage.py runserver

# O servidor inciará na porta:8000 - acesse <http://127.0.0.1:8000/>
```



