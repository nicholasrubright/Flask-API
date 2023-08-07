from http import HTTPStatus
from flask import Blueprint
from src.models import DbMovie, MovieSchema
from src.repository.movie import MovieRepository
movies_bp = Blueprint('movies_bp', __name__, url_prefix='/movies')

@movies_bp.route('/', methods=['GET'])
def get(movieRepository: MovieRepository):
    try:
        data = movieRepository.getAll()
        return data, HTTPStatus.OK
    except Exception as err:
        print("Error: ", err, flush=True)
        return [], HTTPStatus.INTERNAL_SERVER_ERROR