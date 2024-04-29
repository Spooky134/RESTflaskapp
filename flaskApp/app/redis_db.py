import redis
from flask import current_app

def get_redis_connection():
    redis_host = current_app.config['REDIS_HOST']
    redis_port = current_app.config['REDIS_PORT']
    redis_db = current_app.config['REDIS_DB']
    
    r = redis.Redis(host=redis_host, port=redis_port, db=redis_db)
    return r
