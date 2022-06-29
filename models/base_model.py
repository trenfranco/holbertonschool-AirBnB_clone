#!/usr/bin/python3
"""Airbnb clone project"""

import uuid
import datetime

class BaseModel:
    """Base class"""
    def __init__(self, *args, **kwargs):
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
    def __str__(self):
        return(f"[BaseModel] ({self.id}) {self.__dict__}")
    def save(self):
        BaseModel.updated_at = datetime.datetime.now()
    def to_dict(self):
        new = {'__class__': __class__.__name__}
        new2 = {**self.__dict__, **new}
        return new2
