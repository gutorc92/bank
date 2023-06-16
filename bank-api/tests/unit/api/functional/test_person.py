import json
from tests.unit.api.functional import client, PersonFactory, generate_dict_factory



def test_person(client):
    response = client.get('/api/person/')
    assert response.status_code == 200

def test_create_a_person(client, faker):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    PersonDict = generate_dict_factory(PersonFactory)
    person = PersonDict()
    response = client.post('/api/person/', data=json.dumps(person), headers=headers)
    assert response.status_code == 200
    assert response.data