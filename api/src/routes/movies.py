from http import HTTPStatus
from flask import Blueprint, jsonify
from src.models import Movie, MovieSchema
movies_bp = Blueprint('movies_bp', __name__, url_prefix='/movies')

@movies_bp.route('/', methods=['GET'])
def get():
    moviesSchema = MovieSchema()
    movies = [Movie(1, "Test Title"), Movie(2, "Another Movie")]
    data = moviesSchema.dump(movies, many=True)
    
    return data, HTTPStatus.OK