import pytest
import factory
from app import create_app
from app.models.models import Person
from functools import partial
from typing import Any, Dict
from factory import Factory
from factory.base import StubObject

def generate_dict_factory(factory: Factory):
    def convert_dict_from_stub(stub: StubObject) -> Dict[str, Any]:
        stub_dict = stub.__dict__
        for key, value in stub_dict.items():
            if isinstance(value, StubObject):
                stub_dict[key] = convert_dict_from_stub(value)
        return stub_dict

    def dict_factory(factory, **kwargs):
        stub = factory.stub(**kwargs)
        stub_dict = convert_dict_from_stub(stub)
        return stub_dict

    return partial(dict_factory, factory)

class PersonFactory(factory.Factory):
    class Meta:
        model = Person
    
    name = factory.Faker('first_name')
    surname = factory.Faker('last_name')
    id_gov = '08798754123'

@pytest.fixture(scope='session', autouse=True)
def faker_session_locale():
    return ['pt_BR']

@pytest.fixture(autouse=True, scope="module")
def client():
    """Configures the app for testing
    Sets app config variable ``TESTING`` to ``True``
    :return: App for testing
    """

    flask_app = create_app()
    flask_app.config['TESTING'] = True

    print('passou aqui')

    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!
