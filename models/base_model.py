#!/usr/bin/python3

"""
        BaseModel that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            date_format = '%Y-%m-%dT%H:%M:%S.%f'
            i_dict = kwargs.copy()
            del i_dict["__class__"]
            for key in i_dict:
                if key == "created_at" or key == "updated_at":
                    i_dict[key] = datetime.strptime(i_dict[key], date_format)
            self.__dict__ = i_dict
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = {}
        new_dict['__class__'] = self.__class__.__name__
        for attr, val in self.__dict__.items():
            if isinstance(val, datetime):
                val = val.isoformat()
            new_dict[attr] = val
        return new_dict
