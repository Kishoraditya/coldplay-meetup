from werkzeug.contrib.cache import RedisCache
from functools import wraps

cache = RedisCache()

def cache_response(timeout=5 * 60):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            cache_key = f.__name__ + str(args) + str(kwargs)
            rv = cache.get(cache_key)
            if rv is None:
                rv = f(*args, **kwargs)
                cache.set(cache_key, rv, timeout=timeout)
            return rv
        return decorated_function
    return decorator

def optimize_images():
    from PIL import Image
    import os
    
    for filename in os.listdir('static/uploads'):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = f'static/uploads/{filename}'
            with Image.open(image_path) as img:
                img.thumbnail((800, 800))
                img.save(image_path, optimize=True, quality=85)
