from app.extensions import db


class Flat(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), unique=False, nullable=False)
  image_url = db.Column(db.Text(), unique=False, nullable=False)

  def __init__(self, title, image_url):
    self.title = title
    self.image_url = image_url
