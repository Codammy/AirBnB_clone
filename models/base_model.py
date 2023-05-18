#!/usr/bin/python3
import uuid
from datetime import datetime
import storage
"""
        BaseModel that defines all common attributes/methods for other classes
"""


class BaseModel():
    """Defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not None and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                for i, j in self.__dict__.items():
                    if i == k:
                        self.__dict__[i] = v
        else:
            storage.new()

    def __str__(self):
        return f'[BaseModel] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        new_dict = {}
        new_dict['__class__'] = self.__class__.__name__
        for attr, val in self.__dict__.items():
            if attr == 'created_at' or attr == 'updated_at':
                new_dict[attr] = str(val.isoformat())
            else:
                new_dict[attr] = val
        return new_dict
