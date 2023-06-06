from flask import render_template
from app.flats import bp


@bp.route('/')
def index():
  return render_template('flats/index.html')
