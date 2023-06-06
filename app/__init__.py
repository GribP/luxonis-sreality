from flask import Flask, redirect

from config import BaseConfig

from app.extensions import db
from app.utils.scraper.crawler import crawl_flats


def create_app():
  app = Flask(__name__)
  app.config.from_object(BaseConfig)

  db.init_app(app)

  # Register BluePrint
  from app.flats import bp as flats_bp
  app.register_blueprint(flats_bp, url_prefix="/flats")

  @app.route("/")
  def index():
    return redirect("/flats")

  @app.cli.command("migrate")
  def migrate():
    from app.models.flat import Flat as _

    with app.app_context():
      db.drop_all()
      db.create_all()
      db.session.commit()

  @app.cli.command("scrap")
  def scrap():
    crawl_flats()

  return app
