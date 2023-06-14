import json
from tests.unit.api.functional import client

def test_person(client):
    response = client.get('/api/person/')
    assert response.status_code == 200

def test_create_a_person(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    person = {
        'name': 'Teste',
        'surname': 'Testando',
        'id_gov': '08798754123'
    }
    response = client.post('/api/person/', data=json.dumps(person), headers=headers)
    assert response.status_code == 200
    assert response.data