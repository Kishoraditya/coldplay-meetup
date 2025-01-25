#!/bin/bash
set -e

# Load environment variables
source .env.prod

# Update application
git pull origin main

# Build new images
docker-compose -f docker-compose.prod.yml build

# Run database migrations
docker-compose -f docker-compose.prod.yml run --rm app flask db upgrade

# Deploy new containers
docker-compose -f docker-compose.prod.yml up -d

# Cleanup old images
docker image prune -f

# Verify deployment
./scripts/health_check.sh
