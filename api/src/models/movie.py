from src.database import db, ma

class Movie:
    def __init__(self, id: int, title: str):
        self.id = id
        self.title = title

class DbMovie(db.Model):
    __tablename__ = 'Movies'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    
class MovieSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DbMovie