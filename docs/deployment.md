# Deployment Guide

## Prerequisites

- Oracle Cloud Free Tier Account
- Domain Name (from Freenom or similar)
- Docker and Docker Compose
- Git

## Quick Deployment

1. Clone repository

```bash
git clone https://github.com/yourusername/coldplay-meetup.git
cd coldplay-meetup

DEPLOYMENT.md
Configure environment
cp .env.free .env
# Edit .env with your settings

Deploy
bash scripts/quick_deploy.sh

Manual Deployment Steps
Server Setup

Create Oracle Cloud VM
Configure security groups
Setup DNS
Application Setup

Install dependencies
Configure Nginx
Setup SSL certificates
Monitoring

Configure health checks
Setup basic monitoring
Maintenance
Regular backups: bash scripts/backup.sh
Updates: bash scripts/update.sh
Monitoring: Visit /health endpoint
