import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', f'sqlite:///{ basedir }/app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
