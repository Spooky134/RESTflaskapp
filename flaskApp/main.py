from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, db=0)


@app.route('/flaskapp/api/data/<key>', methods=['GET'])
def get(key):
    value = r.get(key)
    if not value:
        return jsonify({'error': 'Not found'}), 404
    return jsonify({'key':key,
                    'value':value.decode('utf-8')})
        

@app.route('/flaskapp/api/data', methods=['POST'])
def post():
    if not request.json or not 'key' in request.json or not 'value' in request.json:
        return jsonify({'error': 'Bad Request'}), 400
    key = request.json['key']
    value = request.json['value']
    r.set(key, value)
    return jsonify({'key':key,
                    'value': value}), 201


@app.route('/flaskapp/api/data/<key>', methods=['PUT'])
def put(key):
    if r.exists(key) == 0:
        return jsonify({'error': 'Not found'}), 404
    if not request.json or not 'value' in request.json:
        return jsonify({'error': 'Bad Request'}), 400
    
    value = request.json['value']
    r.set(key, value)
    return jsonify({'key': key,
                    'value': value}), 200
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
