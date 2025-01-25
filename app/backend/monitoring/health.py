from flask import Blueprint, jsonify
from ..models import db

health_bp = Blueprint('health', __name__)

@health_bp.route('/health')
def health_check():
    status = {
        'database': check_database(),
        'redis': check_redis(),
        'disk_space': check_disk_space()
    }
    
    is_healthy = all(status.values())
    return jsonify(status), 200 if is_healthy else 503

def check_database():
    try:
        db.session.execute('SELECT 1')
        return True
    except Exception:
        return False

from redis import Redis
import psutil

def check_redis(redis_client):
    try:
        redis_client.ping()
        return True
    except:
        return False

def check_disk_space(path="/"):
    disk_usage = psutil.disk_usage(path)
    return disk_usage.percent < 90
