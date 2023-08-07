from sqlalchemy.orm import DeclarativeBase
from flask_marshmallow.sqla import SQLAlchemyAutoSchema
from typing import Type
from flask_marshmallow import Schema


class Base(DeclarativeBase):
    pass

class Model:
    _DatabaseModel = None
    _DatabaseSchema = None
    _Schema = None

    AdditionalKeys = {'DatabaseModel', 'DatabaseSchema', '_Schema'}

    def __init__(self, dbModel: Type[Base] | None = None, dbSchema: Type[SQLAlchemyAutoSchema] | None = None, schema: Type[Schema] | None = None):
        self._DatabaseModel = dbModel
        self._DatabaseSchema = dbSchema
        self._Schema = schema

    def toJSON(self):
        return {k: self.__dict__[k] for k in set(self.__dict__.keys() - self.AdditionalKeys) & set(self.__dict__.keys())}
