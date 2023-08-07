from src.models.movie import Movie
from flask_sqlalchemy import SQLAlchemy
from injector import inject

class MovieRepository:
    movieSchema = Movie._DatabaseSchema()
    
    @inject
    def __init__(self, db: SQLAlchemy):
        self.db = db
    
    def getAll(self):
        movies = self.db.session.execute(self.db.Select(Movie._DatabaseModel)).scalars()
        data = self.movieSchema.dump(movies, many=True)
        return data