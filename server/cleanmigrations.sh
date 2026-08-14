#!/bin/bash

timestamp=$(date +%F-%H:%M)
mkdir -p data/dbbackup/$timestamp/migrations

mv core/migrations data/dbbackup/$timestamp/migrations/core
