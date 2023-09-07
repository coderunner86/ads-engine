from sqlalchemy import Column, String
from .entity import Entity, Base

from marshmallow import Schema, fields

class Result(Entity, Base):
    __tablename__ = 'results'


    ai_copy = Column(String(length=1000))
    status = Column(String(length=20))
    last_updated_by = Column(String(length=255))

    def __init__(self, ai_copy, status, created_by, last_updated_by):
        super().__init__(self, created_by)
        self.ai_copy = ai_copy
        self.status = status
        self.last_updated_by = last_updated_by


# created_by = fields.Str()
class ResultSchema(Schema):
    id = fields.Number()
    ai_copy = fields.Str()
    status = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()