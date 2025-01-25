#!/bin/bash

# Backup databases and configurations
BACKUP_DIR="/backups/$(date +%Y%m%d)"
mkdir -p $BACKUP_DIR

# Database backup
docker-compose exec -T db pg_dump -U postgres app > $BACKUP_DIR/database.sql

# Redis backup
docker-compose exec -T redis redis-cli SAVE
docker cp $(docker-compose ps -q redis):/data/dump.rdb $BACKUP_DIR/

# Configuration files
cp .env* $BACKUP_DIR/
cp docker-compose*.yml $BACKUP_DIR/

# Compress backup
tar -czf $BACKUP_DIR.tar.gz $BACKUP_DIR
