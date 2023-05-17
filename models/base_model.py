#!/usr/bin/python3
import uuid
from datetime import datetime
"""
        BaseModel that defines all common attributes/methods for other classes
"""


class BaseModel():
    """Defines all common attributes/methods for other classes"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f'[BaseModel] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = {}
        new_dict['__class__'] = self.__class__.__name__
        for attr, val in self.__dict__.items():
            if attr == self.created_at or attr == self.updated_at:
                new_dict[attr] = val.isoformat()
                continue
            new_dict[attr] = val
        return new_dict
