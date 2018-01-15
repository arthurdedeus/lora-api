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
        database = input("What is the database?\n1: POSTGRES\n2: MYSQL\n")

    if database == '1':
        print('Adding postgres')
        merge_postgres_branch = "git merge origin/postgres"
        os.system(merge_postgres_branch)
    elif database == '2':
        print('Adding mysql')
        merge_mysql_branch = "git merge origin/mysql"
        os.system(merge_mysql_branch)

    # Auth
    auth = ''
    while auth not in ['1']:
        auth = input("What is the authentication system?\n1: Rest Auth without socials\n")

    if auth == '1':
        print('Adding rest auth without socials')
        merge_auth_branch = "git merge origin/auth"
        os.system(merge_auth_branch)

    print('Finalizing setup')
    merge_dev_branch = "git checkout master && git merge dev"
    os.system(merge_dev_branch)
