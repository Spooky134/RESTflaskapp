import json
from conftest import client, setup_db


def test_get_existing_data(client):
    key = 'test_key'
    value = 'test_value'
    client.post('/flaskapp/api/data', json={'key': key, 'value': value})
    response = client.get(f'/flaskapp/api/data/{key}')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert data['key'] == key
    assert data['value'] == value

def test_get_nonexistent_data(client):
    response = client.get('/flaskapp/api/data/nonexistent_key')
    assert response.status_code == 404
    data = json.loads(response.data.decode('utf-8'))
    assert data['error'] == 'Not found'

def test_post_data(client):
    key = 'test_key'
    value = 'test_value'
    response = client.post('/flaskapp/api/data', json={'key': key, 'value': value})
    assert response.status_code == 201
    data = json.loads(response.data.decode('utf-8'))
    assert data['key'] == key
    assert data['value'] == value

def test_post_invalid_data(client):
    response = client.post('/flaskapp/api/data', json={'invalid': 'data'})
    assert response.status_code == 400
    data = json.loads(response.data.decode('utf-8'))
    assert data['error'] == 'Bad Request'

def test_put_existing_data(client):
    key = 'test_key'
    value = 'test_value'
    client.post('/flaskapp/api/data', json={'key': key, 'value': value})
    new_value = 'new_test_value'
    response = client.put(f'/flaskapp/api/data/{key}', json={'value': new_value})
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert data['key'] == key
    assert data['value'] == new_value

def test_put_nonexistent_data(client):
    response = client.put('/flaskapp/api/data/nonexistent_key', json={'value': 'test_value'})
    assert response.status_code == 404
    data = json.loads(response.data.decode('utf-8'))
    assert data['error'] == 'Not found'

def test_put_invalid_data(client):
    key = 'test_key'
    value = 'test_value'
    client.post('/flaskapp/api/data', json={'key': key, 'value': value})
    response = client.put(f'/flaskapp/api/data/{key}', json={'invalid': 'data'})
    assert response.status_code == 400
    data = json.loads(response.data.decode('utf-8'))
    assert data['error'] == 'Bad Request'
