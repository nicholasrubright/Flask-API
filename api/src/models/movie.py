from typing import Type, Dict
from src.database import Base
from sqlalchemy import Column, Integer, Text
from flask_marshmallow.sqla import SQLAlchemyAutoSchema
from marshmallow import pre_load, Schema, fields

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

class Model:
    DatabaseModel = None
    DatabaseSchema = None
    Schema = None

    AdditionalKeys = {'DatabaseModel', 'DatabaseSchema'}

    def __init__(self, dbModel: Type[Base] | None = None, dbSchema: Type[SQLAlchemyAutoSchema] | None = None):
        self.DatabaseModel = dbModel
        self.DatabaseSchema = dbSchema
        self.Schema = MovieSchema

    def toJSON(self):
        return {k: self.__dict__[k] for k in set(self.__dict__.keys() - self.AdditionalKeys) & set(self.__dict__.keys())}


class Movie(Model):

    DatabaseModel = DbMovie
    DatabaseSchema = DbMovieSchema
    Schema = MovieSchema

    def __init__(self, id: int, title: str):
        self.id = id
        self.title = title



temp = Movie(1, "test title")

print("testing: ", temp.toJSON(), flush=True)