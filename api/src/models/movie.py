from marshmallow_generic import GenericSchema, fields, pre_load

class Movie:
    def __init__(self, id: int, title: str):
        self.id = id
        self.title = title
        
class MovieSchema(GenericSchema[Movie]):
    id = fields.Int()
    title = fields.Str()
    
    @pre_load
    def make_object(self, data, **kwargs):
        return Movie(data["id"], data["title"]).__dict__