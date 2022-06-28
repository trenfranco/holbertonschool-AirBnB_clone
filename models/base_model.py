#!/usr/bin/python3
"""Airbnb clone project"""

import uuid
import datetime

class BaseModel:
    """Base class"""
    def __init__(self):
        BaseModel.id = str(uuid.uuid4())
        BaseModel.created_at = datetime.datetime.now()
        BaseModel.updated_at = datetime.datetime.now()
    def __str__(self):
        return(f"[BaseModel] ({self.id}) {self.to_dict()}")
    def save(self):
        BaseModel.updated_at = datetime.datetime.now()
    def to_dict(self):
        new = {'__class__': __class__.__name__, 'updated_at': self.updated_at.isoformat(), 'id': self.id, 'created_at': self.created_at.isoformat()}
        new2 = {**self.__dict__, **new}
        return new2


