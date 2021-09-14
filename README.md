# LoRa API

API desenvolvida para a disciplina EEL7814 - Projeto Nível I em Telecomunicações I.
A API conta com um endpoint para receber a requisição do webhook da TTN. Através dele, os dados
do dispositivo são recebidos pela API, onde então são registrados no banco de dados da aplicação.

Agradecimento especial à [Jungle Devs](https://github.com/JungleDevs) por disponibilizar o
boilerplate do Django para o desenvolvimento do projeto.

## Requirements

- [Python 3.7](https://www.python.org)
- [Docker](https://www.docker.com)
- [Docker Compose](https://docs.docker.com/compose/)
- [Virtualenv](https://github.com/pypa/virtualenv/)
- [Git](https://git-scm.com/)

## Databases

The options available are:

- POSTGRES
- MYSQL

## Authentication System

We currently have 2 options:

- REST auth
- REST auth with social accounts

        Current providers:
        - Facebook
        - Google

## Setup

To use this boilerplate follow this steps:

- Clone this repository: `git clone https://github.com/JungleDevs/boilerplate-django.git PROJECT_NAME`
- Run: `python setup.py` and follow the steps

Once the setup is done, you'll be able to run the backend:

- Create the virtual environment and activate it

        virtualenv -p python3 venv
        source venv/bin/activate
- Install the requirements `pip install -r requirements.txt`
- Start the dockers `docker-compose up`
- Run the server

You need a `.env`file with your environment variables, here's an example file:
```
LOAD_ENVS_FROM_FILE='True'
ENVIRONMENT='development'
SECRET_KEY='#*=JungleDjangoBoilerplate=*#'
DEFAULT_FROM_EMAIL='Boilerplate <boilerplate@jungledevs.com>'
DATABASE_URL='postgres://postgres:postgres@localhost:5432/boilerplate'
SENTRY_DSN='{sentry_key}'
AWS_STORAGE_BUCKET_NAME='django-be'
```

## Deploy
This project is configured to use Terraform (https://www.terraform.io/) to create the
infrastructure in AWS. You must install the CLI: https://www.terraform.io/downloads.html
The following resources must be created manually:
- S3 bucket to hold terraform state
- EC2 key pair
- HTTPS certificate

After creating the required resources, you need to update the the following fields inside `main.tf`:
- terraform.backend.bucket
- locals.project
- locals.certificate_arn
- locals.key_name

*  You can also change the region and aws machine instance type once needed.

To deploy to the staging environment run:
```
cd infrastructure
terraform init
terraform workspace select staging
terraform apply
```

To create a new environment run:
```
terraform workspace new ENV_NAME
```

Use terraform's format option before committing changes:
```
terraform fmt --recursive
```
