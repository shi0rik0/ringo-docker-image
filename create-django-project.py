#!/usr/bin/python3

import argparse
import os

parser = argparse.ArgumentParser(description='Create a django project.')
parser.add_argument('name', metavar='name', type=str, nargs=1,
                    help='the name of the project')
args = parser.parse_args()

cmd = f'''
docker-compose run web django-admin startproject {args.name[0]} .
'''

for i in cmd.split('\n'):
    os.system(i)
