#!/usr/bin/python3

"""
        BaseModel that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""
    def init(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f'{[self.__class__.__name__}] {(<self.id>}) {<self.__dict__>}'

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = {}
        new_dict['__class__'] = self.__class__.__name__
        for attr, val in self.__dict__:
            if attr == created_at or attr == updated_at:
                new_dict[attr] = val.isoformat()
            new_dict[attr] = val
        return new_dict
