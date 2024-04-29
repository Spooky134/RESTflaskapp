from flask import Blueprint, jsonify, request
from app.redis_db import get_redis_connection

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/data/<key>', methods=['GET'])
def get(key):
    r = get_redis_connection()
    value = r.get(key)
    if not value:
        return jsonify({'error': 'Not found'}), 404
    return jsonify({'key':key,
                    'value':value.decode('utf-8')})
        

@api_bp.route('/api/data', methods=['POST'])
def post():
    if not request.json or not 'key' in request.json or not 'value' in request.json:
        return jsonify({'error': 'Bad Request'}), 400
    key = request.json['key']
    value = request.json['value']
    r = get_redis_connection()
    r.set(key, value)
    return jsonify({'key':key,
                    'value': value}), 201


@api_bp.route('/api/data/<key>', methods=['PUT'])
def put(key):
    r = get_redis_connection()
    if r.exists(key) == 0:
        return jsonify({'error': 'Not found'}), 404
    if not request.json or not 'value' in request.json:
        return jsonify({'error': 'Bad Request'}), 400
    
    value = request.json['value']
    r.set(key, value)
    return jsonify({'key': key,
                    'value': value}), 200