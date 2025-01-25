#!/bin/bash
# One-command deployment script for Oracle Cloud Free Tier

# Clone and setup
git clone https://github.com/yourusername/coldplay-meetup.git
cd coldplay-meetup

# Configure environment
cp .env.free .env
mkdir -p data static/uploads

# Start application
docker-compose -f docker-compose.free.yml up -d

# Setup SSL with Certbot
sudo certbot --nginx -d your-domain.tk

echo "Deployment complete! Visit https://your-domain.tk"
