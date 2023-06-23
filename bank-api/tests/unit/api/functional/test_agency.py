import json
from tests.mocks import AgencyFactory, generate_dict_factory
from tests.unit.api.functional import client

def test_agency(client):
    response = client.get('/api/agency/')
    assert response.status_code == 200

def test_create_a_agency(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'bc_identify': '0001',
        'city': 'Brasilia',
    }
    AgencyDict = generate_dict_factory(AgencyFactory)
    data = AgencyDict()
    response = client.post('/api/agency/', data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    assert response.data