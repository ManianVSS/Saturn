#!/bin/bash

timestamp=$(date +%F-%H:%M)
mkdir -p data/dbbackup/$timestamp/migrations

mv core/migrations data/dbbackup/$timestamp/migrations/core
mv product/migrations data/dbbackup/$timestamp/migrations/product
mv program/migrations data/dbbackup/$timestamp/migrations/program
mv people/migrations data/dbbackup/$timestamp/migrations/people