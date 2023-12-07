#!/bin/python3.8
"""class BaseModel that defines all common attributes/methods for other classes:"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class with public instance attribute of:
    id: string
    created_at: datetime
    updated_at: datetime
    """
    def __init__(self):
        """initializes id to a random id,
        created_at and updated_at to datetime respectively
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def __str__(self):
        """
        should print [<class name>] (<self.id>) <self.__dict__>
        :return:
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    def save(self):
        """saves the content with the updated time"""
        self.updated_at = datetime.now()
    def to_dict(self, *args, **kwargs):
        """returns a dictionary containing all key/values of {self}"""
        to_dict = self.__dict__
        to_dict['__class__'] = self.__class__.__name__
        to_dict['updated_at'] = datetime.isoformat(to_dict['updated_at'])
        to_dict['created_at'] = datetime.isoformat(to_dict['created_at'])
        return to_dict