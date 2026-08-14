#!/bin/bash

timestamp=$(date +%F-%H:%M)
mkdir -p data/dbbackup/$timestamp/migrations

mv core/migrations data/dbbackup/$timestamp/migrations/core

mv data/db.sqlite3 data/dbbackup/$timestamp
mv product/migrations data/dbbackup/$timestamp/migrations/product
mv program/migrations data/dbbackup/$timestamp/migrations/program

bash migrate.sh
python manage.py create_super_user
python manage.py create_default_configuration