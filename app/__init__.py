from flask import Flask

from config import BaseConfig

from app.extensions import db


def create_app():
  app = Flask(__name__)
  app.config.from_object(BaseConfig)

  db.init_app(app)

  @app.cli.command("migrate")
  def migrate():
    from app.models.flat import Flat as _

    with app.app_context():
      db.drop_all()
      db.create_all()
      db.session.commit()

  return app
