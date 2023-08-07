from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()

ma = Marshmallow()