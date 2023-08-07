from http import HTTPStatus
from flask import Blueprint, jsonify

movies_bp = Blueprint('movies_bp', __name__, url_prefix='/movies')

@movies_bp.route('/', methods=['GET'])
def get():
    return jsonify({
        "hello": "world"
    })