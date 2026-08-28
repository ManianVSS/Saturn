#!/bin/bash

python3 manage.py makemigrations core
python3 manage.py makemigrations product
python3 manage.py makemigrations program
python3 manage.py makemigrations people
python3 manage.py migrate
