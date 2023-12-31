from flask import Flask, redirect, url_for
from src.routes import api_bp
from config import Config
from injector import Module, Injector, singleton, provider
from flask_sqlalchemy import SQLAlchemy
from flask_injector import FlaskInjector
from src.repository.movie import MovieRepository
from src.services import MovieService


class AppModule(Module):
    def __init__(self, app):
        self.app = app
    
    @provider
    @singleton
    def provide_SQLAlchemy(self) -> SQLAlchemy:
        return SQLAlchemy(self.app)
    
    def configure(self, binder):
        movieRepository = MovieRepository(self.provide_SQLAlchemy())
        binder.bind(MovieRepository, to=movieRepository, scope=singleton)
        movieService = MovieService()
        binder.bind(MovieService, to=movieService, scope=singleton)


def create_app(name: str) -> Flask:
    app = Flask(name)
    app.config.from_object(Config)
    app.url_map.strict_slashes = False
    app.debug = True
    
    # Ensure that blueprints are added before initializing injector
    app.register_blueprint(api_bp, url_prefix='/api')
    
    @app.route('/')
    def index():
        return redirect(url_for('api_bp.index'))
    
    with app.app_context():
        injector = Injector([AppModule(app)])
    
    FlaskInjector(app=app, injector=injector)
    
    return app