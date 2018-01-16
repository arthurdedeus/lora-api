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

    print('Finalizing setup')
    merge_dev_branch = "git checkout master && " \
                       "git merge dev --no-edit && " \
                       "rm -rf .git && " \
                       "rm -rf setup.py"
    os.system(merge_dev_branch)
