import json
from tests.mocks import AccountFactory, generate_dict_factory
from tests.unit.api.functional import client, headers

def test_account(client):
    response = client.get('/api/account/')
    assert response.status_code == 200

def test_create_a_account(client, headers):
    AccountDict = generate_dict_factory(AccountFactory)
    data = AccountDict()
    response = client.post('/api/account/', data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    assert response.data

