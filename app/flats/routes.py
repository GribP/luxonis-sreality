from flask import jsonify

from app.flats import bp
from app.models.flat import Flat


@bp.route('/')
def index():
  def parse_data(flat: Flat):
    return {
      "id": flat.id,
      "title": flat.title,
      "image_url": flat.image_url,
    }

  return jsonify(list(map(parse_data, Flat.query.all())))
