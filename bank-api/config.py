import os
from dotenv import load_dotenv, find_dotenv

print(os.environ.get("SECRET_KEY"))

SQLALCHEMY_DATABASE_URI = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=os.environ.get("DB_USER"),
        passwd=os.environ.get("DB_PASS"),
        host=os.environ.get("DB_HOST"),
        port=os.environ.get("DB_PORT"),
        db=os.environ.get("DB_NAME"))
class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = 'postgresql:///wordcount_dev"'

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI