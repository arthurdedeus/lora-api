#!/usr/bin/env python
###
# Libraries
###
import os
import sys
import signal
import re


# SIGTERM
###
def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    delete_dev_branch = "git checkout master && git branch -D dev"
    os.system(delete_dev_branch)
    sys.exit(0)


###
# Constants
###
CURR_DIR = os.getcwd()
NON_BOILERPLATE_FOLDERS = ['/.git', '/.vscode', '/.idea']
NON_BP_FLD_PATH = [CURR_DIR + fld for fld in NON_BOILERPLATE_FOLDERS]
CELERY_EXCLUSIVE_FILES = ['settings/celery.py', 'settings/celeryconfig.py']
WEBSOCKETS_EXCLUSIVE_FILES = ['settings/asgi.py', 'settings/consumer.py', 'settings/routing.py',
                              'helpers/custom_auth_middleware.py']
SOCIALS_EXCLUSIVE_FILES = ['accounts/custom_providers.py']

###
# Setup boilerplate
###
if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    if sys.version_info[0] < 3:
        name = raw_input('What is the project name (no spaces, display name)?\n')
        use_celery = True if raw_input('Is this project using Celery? [y/N]\n') == 'y' else False
        use_websockets = True if raw_input('Is this project using WebSockets [y/N]\n') == 'y' else False
        use_socials = True if raw_input(
            'Is this project using Social Accounts (e.g. Google, Facebook)? [y/N]\n') == 'y' else False

    else:
        name = input('What is the project name (no spaces, display name)?\n')
        use_celery = True if input('Is this project using Celery? [y/N]\n') == 'y' else False
        use_websockets = True if input('Is this project using WebSockets [y/N]\n') == 'y' else False
        use_socials = True if input(
            'Is this project using Social Accounts (e.g. Google, Facebook)? [y/N]\n') == 'y' else False

    use_redis = use_celery or use_websockets
    FILES_TO_DELETE = list()
    if not use_celery:
        FILES_TO_DELETE += CELERY_EXCLUSIVE_FILES
    if not use_websockets:
        FILES_TO_DELETE += WEBSOCKETS_EXCLUSIVE_FILES
    if not use_socials:
        FILES_TO_DELETE += SOCIALS_EXCLUSIVE_FILES

    if name:
        print('Customizing the boilerplate')

        for root, dirs, files in os.walk(CURR_DIR):
            check_substring = [1 for folder in NON_BP_FLD_PATH if folder in root]
            if sum(check_substring) == 0:
                for filename in files:

                    if '/'.join([root.replace(CURR_DIR + '/', ''), filename]) in FILES_TO_DELETE:
                        os.remove(root + '/' + filename)
                        continue

                    if 'setup.py' not in filename:
                        if sys.version_info[0] < 3:
                            file = open(root + '/' + filename, 'r')
                        else:
                            file = open(root + '/' + filename, 'r', encoding='utf-8')
                        text = str(file.read())
                        file.close()
                        text = text.replace('Django Boilerplate', name)
                        text = text.replace('boilerplate-django', name.lower() + '-django')
                        text = text.replace('boilerplate', name.lower())
                        text = text.replace('Boilerplate', name)

                        if use_redis:
                            text = re.sub(r'\n?#<redis>([\s\S]*?)\n#</redis>', r'\1', text)
                        else:
                            text = re.sub(r'\n?#<redis>([\s\S]*?)\n#</redis>', '', text)
                        if use_celery:
                            text = re.sub(r'\n?#<celery>([\s\S]*?)\n#</celery>', r'\1', text)
                        else:
                            text = re.sub(r'\n?#<celery>([\s\S]*?)\n#</celery>', '', text)
                        if use_websockets:
                            text = re.sub(r'\n?#<websockets>([\s\S]*?)\n#</websockets>', r'\1', text)
                        else:
                            text = re.sub(r'\n?#<websockets>([\s\S]*?)\n#</websockets>', '', text)
                        if use_socials:
                            text = re.sub(r'\n?#<socials>([\s\S]*?)\n#</socials>', r'\1', text)
                        else:
                            text = re.sub(r'\n?#<socials>([\s\S]*?)\n#</socials>', '', text)

                        if sys.version_info[0] < 3:
                            file = open(root + '/' + filename, 'r')
                        else:
                            file = open(root + '/' + filename, 'r', encoding='utf-8')
                        if sys.version_info[0] < 3:
                            file = open(root + '/' + filename, 'w')
                        else:
                            file = open(root + '/' + filename, 'w', encoding='utf-8')
                        file.write(text)
                        file.close()

    readme_file = open('README.md', 'w+')
    if name:
        readme_name = name + ' Django'
    else:
        readme_name = 'Django Project'
    readme_file.write(
        '''# {}

## Requirements

- [Python 3.9](https://www.python.org)
- [Docker](https://www.docker.com)
- [Docker Compose](https://docs.docker.com/compose/)
- [Virtualenv](https://github.com/pypa/virtualenv/)
- [Git](https://git-scm.com/)

## Development

- Create the virtual environment and activate it

        virtualenv -p python3 venv
        source venv/bin/activate
- Install the requirements `pip install -r requirements.txt`
- Start the dockers `docker-compose up` with the database and the localstack
- Run the server with `python manage.py runserver 8000`

You need a `.env`file with your environment variables, here's an example file:
```
LOAD_ENVS_FROM_FILE='True'
ENVIRONMENT='development'
SECRET_KEY='secret_key'
DEFAULT_FROM_EMAIL='Boilerplate <boilerplate@jungledevs.com>'
DATABASE_URL='postgres://postgres:postgres@localhost:5432/boilerplate'
SENTRY_DSN='sentry_key'
REDIS_HOST=localhost
REDIS_PORT=6379
AWS_STORAGE_BUCKET_NAME='django-be'
```
        '''.format(readme_name)
    )
    readme_file.close()

    print('Finalizing setup')
    merge_dev_branch = "rm -rf .git && " \
                       "rm -rf setup.py &&" \
                       "mv env.example .env"
    os.system(merge_dev_branch)
