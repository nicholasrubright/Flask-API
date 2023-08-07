from flask import Flask, redirect, url_for
from src.routes import api_bp
from src.database import db, ma
from config import Config


def create_app(name: str) -> Flask:
    app = Flask(name)
    app.config.from_object(Config)
    app.url_map.strict_slashes = False
    
    db.init_app(app)
    ma.init_app(app)
    
    app.register_blueprint(api_bp, url_prefix='/api')
    
    @app.route('/')
    def index():
        return redirect(url_for('api_bp.index'))
    
    return app