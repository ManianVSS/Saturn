#!/bin/bash

python3 manage.py makemigrations core
python3 manage.py migrate
