import json
from tests.unit.api.functional import client

def test_account(client):
    response = client.get('/api/account/')
    assert response.status_code == 200

def test_create_a_account(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'bc_identify': '455465',
        'type': 'current',
        'person': 1,
        'agency': 1
    }
    response = client.post('/api/account/', data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    assert response.data
    data = {
        'bc_identify': '455466',
        'type': 'saving',
        'person': 1,
        'agency': 1
    }
    response = client.post('/api/account/', data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    assert response.data

