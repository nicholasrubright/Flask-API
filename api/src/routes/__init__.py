from flask import Blueprint

from src.routes.movies import movies_bp

api_bp = Blueprint('api_bp', __name__)

@api_bp.route("/", methods=['GET'])
def index():
    return "<h1>Flask API</h1>"

api_bp.register_blueprint(movies_bp)