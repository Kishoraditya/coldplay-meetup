# Optimized for Oracle Cloud Free Tier
workers = 2
threads = 4
bind = "0.0.0.0:8000"
worker_class = "gevent"
max_requests = 1000
timeout = 30
keepalive = 2
