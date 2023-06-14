import json
from tests.unit.api.functional import client

def test_list_transaction(client):
    response = client.get('/api/transaction/')
    assert response.status_code == 200

def test_create_a_transaction(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'account': '455465',
        'date': '12/06/2022',
        'value': 1000.00,
        'account': 1,
    }
    response = client.post('/api/transaction/deposit', data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    assert response.data
    data = {
        'account': '455465',
        'date': '12/06/2022',
        'value': 500.00,
        'account': 1,
    }
    response = client.post('/api/transaction/draw', data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    assert response.data

def test_create_a_transfer(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'date': '12/06/2022',
        'value': 200.00,
        'account_origin': 1,
        'account_receiver': 2
    }
    response = client.post('/api/transaction/transfer', data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    assert response.data

