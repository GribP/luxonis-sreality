from flask import Flask

from config import BaseConfig

from app.extensions import db


def create_app():
  app = Flask(__name__)
  app.config.from_object(BaseConfig)

  db.init_app(app)

  return app
