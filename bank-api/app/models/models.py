import datetime as dt
from app.extensions import db
from sqlalchemy import Enum

class BaseMixInModel(object):
    def __iter__(self):
      for x in self.__class__.__table__.columns:
          yield x.name, self.__getattribute__(x.name)

    @staticmethod
    def json_type(x):
        if isinstance(x, dt.datetime):
            return x.timestamp()
        return x
    
    def json(self, exclude=()):
        return {k: self.json_type(v) for k, v in dict(self).items() if k not in exclude}

class Person(db.Model, BaseMixInModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    id_gov = db.Column(db.String, nullable=False)


    def __init__(self, name : str, surname: str, id_gov: str):
        self.name = name
        self.surname = surname
        self.id_gov = id_gov

    def __repr__(self):
        return f"<Person {self.name}>"

class Agency(db.Model, BaseMixInModel):
    id = db.Column(db.Integer, primary_key=True)
    bc_identify = db.Column(db.String, nullable=False, unique=True)
    city = db.Column(db.String, nullable=False)


    def __init__(self, bc_identify : str, city: str):
        self.bc_identify = bc_identify
        self.city = city

    def __repr__(self):
        return f"<Agency {self.bc_identify}>"

class Account(db.Model, BaseMixInModel):
    id = db.Column(db.Integer, primary_key=True)
    bc_identify = db.Column(db.String, nullable=False, unique=True)
    type = db.Column(Enum("current", "saving", name="account_type", create_type=True), nullable=False)
    person_owner = db.Column(db.Integer, db.ForeignKey('person.id'),
                          nullable=False)
    agency_owner = db.Column(db.Integer, db.ForeignKey('agency.id'),
                          nullable=False)

    def __init__(self, bc_identify : str, type: str):
        self.bc_identify = bc_identify
        self.type = type

    def __repr__(self):
        return f"<Agency {self.bc_identify}>"

class Balance(db.Model, BaseMixInModel):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                          nullable=False, unique=True)
    value = db.Column(db.Float, nullable=False)

    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return f"<Balance {self.value}>"

class Transaction(db.Model, BaseMixInModel):
    id = db.Column(db.Integer, primary_key=True)
    type_of = db.Column(Enum("credit", "charge", name="transaction_type", create_type=True)) 
    date = db.Column(db.DateTime)
    value = db.Column(db.Float, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                          nullable=False)

    def __init__(self, type_of: str, date: str, value: float, account_id : int):
        self.type_of = type_of
        self.date = date
        self.value = value
        self.account_id = account_id

    def __repr__(self):
        return f"<Transaction {self.account_id}>"
