from app.extensions import db
from sqlalchemy import Enum

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    id_gov = db.Column(db.String, nullable=False)


    def __init__(self, name : str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"<Stock {self.name}>"

class Agency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bc_identify = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)


    def __init__(self, bc_identify : str, city: str):
        self.bc_identify = bc_identify
        self.city = city

    def __repr__(self):
        return f"<Stock {self.bc_identify}>"

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bc_identify = db.Column(db.String, nullable=False)
    type = db.Column(Enum("current", "saving", name="account_type", create_type=True), nullable=False)


    def __init__(self, bc_identify : str, type: str):
        self.bc_identify = bc_identify
        self.type = type

    def __repr__(self):
        return f"<Stock {self.bc_identify}>"

class Transaction(db.Model):
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
