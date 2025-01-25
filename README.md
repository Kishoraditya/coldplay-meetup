
# Frontend

Tailwind CSS (styling)
Alpine.js (reactivity)
DaisyUI (UI components)
PWA capabilities
Backend:

Flask (web framework)
SQLite (database)
Redis (caching)
Gunicorn (WSGI server)
Nginx (reverse proxy)
Infrastructure:

Oracle Cloud Free Tier (VM)
Cloudflare (CDN & SSL)
Freenom (domain)
GitHub Actions (CI/CD)
Docker & Docker Compose
Certbot (SSL certificates)
Monitoring:

Prometheus (metrics)
Grafana (dashboards)
Sentry (error tracking)
Security:

JWT (authentication)
bcrypt (password hashing)
rate-limiter (DDoS protection)
CSP headers
ARCHITECTURE:
Client Request → Cloudflare → Nginx → Gunicorn → Flask App ↔ Redis Cache
                                                         ↔ SQLite DB
                                                         ↔ File Storage

coldplay-meetup/
├── .github/
│   └── workflows/
│       └── deploy.yml
├── app/
│   ├── backend/
│   │   ├── __init__.py
│   │   ├── auth/
│   │   ├── profiles/
│   │   ├── matches/
│   │   └── utils/
│   ├── frontend/
│   │   ├── static/
│   │   └── templates/
│   └── tests/
├── config/
│   ├── nginx.conf
│   ├── gunicorn.conf.py
│   └── prometheus.yml
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── scripts/
│   ├── setup.sh
│   ├── deploy.sh
│   └── backup.sh
├── .env.example
├── requirements.txt
└── README.md

coldplay-meetup/
├── app/
│   ├── backend/
│   │   ├── __init__.py
│   │   ├── auth/
│   │   ├── profiles/
│   │   ├── matches/
│   │   └── utils/
│   ├── frontend/
│   │   ├── static/
│   │   │   ├── css/
│   │   │   ├── js/
│   │   │   └── images/
│   │   └── templates/
│   └── tests/
│       ├── conftest.py
│       ├── test_auth.py
│       ├── test_matches.py
│       ├── test_profiles.py
│       ├── test_security.py
│       └── performance/
│           ├── locustfile.py
│           └── benchmark.py
├── config/
│   ├── nginx.free.conf
│   ├── gunicorn_free.py
│   ├── prometheus/
│   │   └── alerts.yml
│   └── grafana/
│       └── dashboards/
├── docs/
│   ├── api_documentation.py
│   └── DEVELOPMENT.md
├── scripts/
│   ├── quick_deploy.sh
│   ├── free_deploy.sh
│   ├── backup_restore.sh
│   ├── cost_optimization.py
│   └── security_hardening.py
├── infrastructure/
│   └── terraform/
│       └── security.tf
├── .github/
│   └── workflows/
│       └── main.yml
├── docker-compose.free.yml
├── Dockerfile
├── requirements.txt
└── .env.free
