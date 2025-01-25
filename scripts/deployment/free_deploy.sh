#!/bin/bash
# Oracle Cloud Free Tier Deployment Script

# Update system
sudo apt update && sudo apt upgrade -y

# Install required packages
sudo apt install -y python3-pip nginx docker.io docker-compose

# Setup application
git clone https://github.com/yourusername/coldplay-meetup.git
cd coldplay-meetup

# Configure environment
cp .env.example .env
# Generate secret key
echo "SECRET_KEY=$(openssl rand -hex 32)" >> .env

# Start services
docker-compose -f docker-compose.free.yml up -d

# Configure Nginx
sudo cp config/nginx.free.conf /etc/nginx/sites-available/coldplay-meetup
sudo ln -s /etc/nginx/sites-available/coldplay-meetup /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl restart nginx
