import os
from dotenv import load_dotenv, find_dotenv

print(os.environ.get("SECRET_KEY"))
class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = 'postgresql:///wordcount_dev"'

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Postgres2022!@localhost:5432/bank'