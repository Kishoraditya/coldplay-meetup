#!/bin/bash

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backups"

# Create backup directory
mkdir -p $BACKUP_DIR

# Backup SQLite database
cp data/app.db $BACKUP_DIR/db_backup_$TIMESTAMP.db

# Backup Redis data
docker-compose exec redis redis-cli SAVE
cp data/redis/dump.rdb $BACKUP_DIR/redis_backup_$TIMESTAMP.rdb

# Compress backups
tar -czf $BACKUP_DIR/backup_$TIMESTAMP.tar.gz $BACKUP_DIR/db_backup_$TIMESTAMP.db $BACKUP_DIR/redis_backup_$TIMESTAMP.rdb

# Clean up old backups (keep last 7 days)
find $BACKUP_DIR -name "backup_*.tar.gz" -mtime +7 -delete
