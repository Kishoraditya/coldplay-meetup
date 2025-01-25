#!/bin/bash

# Update system packages
sudo apt update && sudo apt upgrade -y

# Pull latest changes
git pull origin main

# Build and restart containers
docker-compose -f docker-compose.yml -f docker-compose.monitoring.yml down
docker-compose -f docker-compose.yml -f docker-compose.monitoring.yml build
docker-compose -f docker-compose.yml -f docker-compose.monitoring.yml up -d

# Run database migrations
docker-compose exec app flask db upgrade

# Clear Redis cache
docker-compose exec redis redis-cli FLUSHALL

# Reload Nginx
docker-compose exec nginx nginx -s reload
