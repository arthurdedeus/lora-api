# Django Boilerplate

This is the JungleDevs boilerplate for Django Applications. \
It uses Django 2.1.9 + Docker. Two options of databases are currently supported. The basic structure for authentication is provided, as well as the support for authentication using social accounts. We are also using [localstack](https://github.com/localstack/localstack) to emulate AWS S3 services.

## Requirements

- [Python 3.6](https://www.python.org)
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

        virtualenv -p Python3.6 venv
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
