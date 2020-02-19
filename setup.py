#!/usr/bin/env python
###
# Libraries
###
import os
import sys
import signal


###
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

###
# Setup boilerplate
###
if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    print('Creating dev branch..')
    create_dev_branch = "git fetch --all && git checkout -b dev"
    os.system(create_dev_branch)

    # Database
    database = ''
    while database not in ['1', '2']:
        database = str(input(
            "What is the database?\n"
            "1: POSTGRES\n"
            "2: MYSQL\n"
        ))

    if database == '1':
        print('Adding postgres')
        merge_postgres_branch = "git merge origin/postgres --no-edit"
        os.system(merge_postgres_branch)
    elif database == '2':
        print('Adding mysql')
        merge_mysql_branch = "git merge origin/mysql --no-edit"
        os.system(merge_mysql_branch)

    # Auth
    auth = ''
    while auth not in ['1', '2']:
        auth = str(input(
            "What is the authentication system?\n"
            "1: Rest Auth without socials\n"
            "2: Rest Auth with socials\n"
        ))

    if auth == '1':
        print('Adding rest auth without socials')
        merge_auth_branch = "git merge origin/auth --no-edit"
        os.system(merge_auth_branch)

    elif auth == '2':
        print('Adding rest auth with socials')
        merge_auth_branch = "git merge origin/auth-social --no-edit"
        os.system(merge_auth_branch)

        provider = ''
        while provider not in ['1', '2', '3']:
            provider = str(input(
                "What are the providers?\n"
                "1: Facebook\n"
                "2: Google\n"
                "3: Facebook + Google\n"
            ))

        if provider == '1':
            print('Adding facebook provider')
            merge_provider_branch = "git merge origin/auth-social-facebook --no-edit"
            os.system(merge_provider_branch)

        elif provider == '2':
            print('Adding google provider')
            merge_provider_branch = "git merge origin/auth-social-google --no-edit"
            os.system(merge_provider_branch)

        elif provider == '3':
            print('Adding facebook and google providers')
            merge_provider_branch = "git merge origin/auth-social-facebook-google --no-edit"
            os.system(merge_provider_branch)

    checkout_master = "git checkout master && git merge dev --no-edit"
    os.system(checkout_master)
    if sys.version_info[0] < 3:
        name = raw_input('What is the project name (no spaces)?\n')
    else:
        name = input('What is the project name (no spaces)?\n')

    if name:
        print('Customizing the boilerplate')

        for root, dirs, files in os.walk(CURR_DIR):
            check_substring = [1 for folder in NON_BP_FLD_PATH if folder in root]
            if sum(check_substring) == 0:
                for filename in files:
                    if 'setup.py' not in filename:
                        file = open(root + '/' + filename, 'r')
                        text = str(file.read())
                        file.close()
                        text = text.replace('Django Boilerplate', name)
                        text = text.replace('boilerplate-django', name.lower() + '-django')
                        text = text.replace('boilerplate', name.lower())
                        text = text.replace('Boilerplate', name)
                        file = open(root + '/' + filename, 'w')
                        file.write(text)
                        file.close()

    readme_file = open('README.md', 'w+')
    if name:
        readme_name = f'{name} Django'
    else:
        readme_name = 'Django Project'
    readme_file.write(
        f'''# {readme_name}

## Requirements

- [Python 3.7](https://www.python.org)
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
SECRET_KEY='#*=JungleDjangoBoilerplate=*#'
DEFAULT_FROM_EMAIL='Boilerplate <boilerplate@jungledevs.com>'
DATABASE_URL='postgres://postgres:postgres@localhost:5432/boilerplate'
SENTRY_DSN='sentry_key'
AWS_STORAGE_BUCKET_NAME='django-be'
```
        '''
    )
    readme_file.close()

    print('Finalizing setup')
    merge_dev_branch = "rm -rf .git && " \
                       "rm -rf setup.py"
    os.system(merge_dev_branch)
