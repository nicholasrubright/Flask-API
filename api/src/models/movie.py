from typing import Dict
from src.database import Base
from sqlalchemy import Column, Integer, Text
from flask_marshmallow.sqla import SQLAlchemyAutoSchema
from marshmallow import pre_load, Schema, fields
from src.database import Model


class DbMovie(Base):
    __tablename__ = 'movies'
    
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    
class DbMovieSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = DbMovie

class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()

    @pre_load
    def make_object(self, data, **kwargs) -> Dict:
        return Movie(data["id"], data["title"]).toJSON()

class Movie(Model):

    _DatabaseModel = DbMovie
    _DatabaseSchema = DbMovieSchema
    _Schema = MovieSchema

    def __init__(self, id: int, title: str):
        self.id = id
        self.title = title



temp = Movie(1, "test title")

print("testing: ", temp.toJSON(), flush=True)