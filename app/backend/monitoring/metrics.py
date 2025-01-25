from prometheus_client import Counter, Gauge, Histogram
from functools import wraps
import time

# Metrics
REQUEST_COUNT = Counter(
    'request_count_total',
    'Total request count',
    ['method', 'endpoint', 'status']
)

ACTIVE_USERS = Gauge(
    'active_users_total',
    'Number of active users'
)

MATCH_LATENCY = Histogram(
    'match_latency_seconds',
    'Time spent processing matches'
)

def track_request(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        start_time = time.time()
        response = f(*args, **kwargs)
        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.endpoint,
            status=response.status_code
        ).inc()
        return response
    return decorated_function
