from src.database import Base
from sqlalchemy import Column, Integer, Text
from flask_marshmallow.sqla import SQLAlchemyAutoSchema

class DbMovie(Base):
    __tablename__ = 'movies'
    
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    
class MovieSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = DbMovie