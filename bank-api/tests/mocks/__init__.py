from app.models.models import Person, Agency, Account
import factory
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

class AgencyFactory(factory.Factory):
    class Meta:
        model = Agency
    
    bc_identify = factory.Sequence(lambda n: f'{n:04d}')
    city = 'Brasília'

class AccountFactory(factory.Factory):
    class Meta:
        model = Account
    
    bc_identify = factory.Sequence(lambda n: f'{n:06d}')
    type = factory.Iterator(["current", "saving"])
    person_owner = factory.SubFactory(PersonFactory)
    agency_owner = factory.SubFactory(AgencyFactory)