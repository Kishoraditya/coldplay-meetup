#!/bin/bash
set -e

# Check application health
APP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/health)
if [ $APP_STATUS -ne 200 ]; then
    echo "Application health check failed with status: $APP_STATUS"
    exit 1
fi

# Check Redis connection
REDIS_STATUS=$(redis-cli ping)
if [ "$REDIS_STATUS" != "PONG" ]; then
    echo "Redis health check failed"
    exit 1
fi

# Check disk space
DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
if [ $DISK_USAGE -gt 90 ]; then
    echo "Warning: Disk usage is above 90%"
    exit 1
fi

echo "All health checks passed successfully"
