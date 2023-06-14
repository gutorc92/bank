import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from flask_cors import CORS
from app.extensions import db
from app.main import bp as main_bp
from app.models.models import *
# from app.transaction import bp as transaction_bp

# main_bp.register_blueprint(transaction_bp, url_prefix='/transaction')


def create_app(config_class=Config):
  # create the app
  app = Flask(__name__)
  CORS(app)
  env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
  app.config.from_object(env_config)

  db.init_app(app)
  migrate = Migrate(app, db)
    
  app.register_blueprint(main_bp, url_prefix='/api')

  @app.route('/test/')
  def test_page():
      return '<h1>Testing the Flask Application Factory Pattern</h1>'
  return app