from http import HTTPStatus
from flask import Blueprint
from src.models import DbMovie, MovieSchema
from flask_sqlalchemy import SQLAlchemy
movies_bp = Blueprint('movies_bp', __name__, url_prefix='/movies')

@movies_bp.route('/', methods=['GET'])
def get(db: SQLAlchemy):
    try:
        movies = db.session.execute(db.Select(DbMovie)).scalars()
        moviesSchema = MovieSchema()
        data = moviesSchema.dump(movies, many=True)
        return data, HTTPStatus.OK
    except Exception as err:
        print("Error: ", err, flush=True)
        return [], HTTPStatus.INTERNAL_SERVER_ERROR