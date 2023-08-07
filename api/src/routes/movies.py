from http import HTTPStatus
from flask import Blueprint
from src.models import DbMovie, MovieSchema
movies_bp = Blueprint('movies_bp', __name__, url_prefix='/movies')

@movies_bp.route('/', methods=['GET'])
def get():
    from src.app import db
    try:
        moviesSchema = MovieSchema()
        movies = db.session.execute(db.Select(DbMovie)).scalars()
        data = moviesSchema.dump(movies)
        return data, HTTPStatus.OK
    except:
        return [], HTTPStatus.INTERNAL_SERVER_ERROR