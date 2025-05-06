## Esse projeto é uma simples calculadora de valor crítico de artefatos para o Genshin Inpact.

### Para iniciar o projeto, apenas execute 

#### Subindo o docker

```docker-compose up -d```

#### Instalando o poetry

```poetry install```

#### Executando as migrations

```
poetry run python manage.py makemigrations

poetry run python manage.py migrate
```

#### Criando um superusuário

```
poetry run python manage.py createsuperuser
```

#### Executando o projeto

```
poetry run python manage.py runserver
```

## Imagem do projeto localmente
![Captura de tela de 2025-05-06 02-57-05](https://github.com/user-attachments/assets/d55d26bd-ff26-4ecd-9b6c-1903ffee9120)
