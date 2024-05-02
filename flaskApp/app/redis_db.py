import redis
import os

def get_redis_connection():
    redis_host = os.getenv('REDIS_HOST')
    redis_port = int(os.getenv('REDIS_PORT'))
    redis_db = int(os.getenv('REDIS_DB'))
    
    r = redis.Redis(host=redis_host, port=redis_port, db=redis_db)
    return r
