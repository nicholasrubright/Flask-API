from src.models import MovieSchema, DbMovie
from flask_sqlalchemy import SQLAlchemy
from injector import inject

class MovieRepository:
    movieSchema = MovieSchema()
    
    @inject
    def __init__(self, db: SQLAlchemy):
        self.db = db
    
    def getAll(self):
        movies = self.db.session.execute(self.db.Select(DbMovie)).scalars()
        data = self.movieSchema.dump(movies, many=True)
        return data