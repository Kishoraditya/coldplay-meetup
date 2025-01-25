from flask import request, jsonify
from redis import Redis
import time

redis_client = Redis(host='redis', port=6379, db=0)

class RateLimiter:
    def __init__(self, requests_per_minute=60):
        self.requests_per_minute = requests_per_minute
        self.window_size = 60  # 1 minute

    def is_allowed(self, key):
        current = int(time.time())
        window_key = f'{key}:{current // self.window_size}'
        
        pipeline = redis_client.pipeline()
        pipeline.incr(window_key)
        pipeline.expire(window_key, self.window_size)
        current_requests = pipeline.execute()[0]
        
        return current_requests <= self.requests_per_minute

def rate_limit(f):
    limiter = RateLimiter()
    
    def decorated_function(*args, **kwargs):
        key = f"rate_limit:{request.remote_addr}"
        
        if not limiter.is_allowed(key):
            return jsonify({
                'error': 'Rate limit exceeded',
                'retry_after': 60
            }), 429
            
        return f(*args, **kwargs)
    
    return decorated_function
