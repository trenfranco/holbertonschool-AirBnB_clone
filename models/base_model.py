#!/usr/bin/python3
"""Airbnb clone project"""

import uuid
import datetime
import models


class BaseModel:
    """Base class"""
    def __init__(self, *args, **kwargs):
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        BaseModel.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        new = {'__class__': __class__.__name__}
        new2 = {**self.__dict__, **new}
        new2["created_at"] = new2["created_at"].isoformat()
        new2["updated_at"] = new2["updated_at"].isoformat()
        return new2
