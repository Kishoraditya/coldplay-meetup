#!/bin/bash

# Start locust with 1000 users, spawn rate 10 users/second
locust -f tests/performance/locustfile.py --headless \
    --users 1000 \
    --spawn-rate 10 \
    --host http://localhost:8000 \
    --run-time 30m \
    --html report.html
