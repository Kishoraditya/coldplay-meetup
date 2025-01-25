from flask import request, abort
from functools import wraps
import hmac
import hashlib
from flask import current_app
import time

def generate_csrf_token(user_id):
    secret = current_app.config['SECRET_KEY']
    timestamp = str(int(time.time()))
    message = f"{user_id}:{timestamp}"
    signature = hmac.new(
        secret.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()
    return f"{message}:{signature}"

def verify_csrf_token(token):
    try:
        message, signature = token.rsplit(':', 1)
        expected_signature = hmac.new(
            current_app.config['SECRET_KEY'].encode(),
            message.encode(),
            hashlib.sha256
        ).hexdigest()
        return hmac.compare_digest(signature, expected_signature)
    except:
        return False

def csrf_protected(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('X-CSRF-Token')
        if not token or not verify_csrf_token(token):
            abort(403)
        return f(*args, **kwargs)
    return decorated_function
