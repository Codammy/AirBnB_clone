#!/usr/bin/python3

"""
    Test module for base_model.py
"""

BaseModel = __import__('models.base_model').BaseModel
import uuid
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test suite for the BaseModel class"""
    def test_checkattr(self):
        """Checks for existence of attributes"""
        basemodel1 = BaseModel()
        self.assertTrue(hasattr(basemodel1, 'created_at'))
        self.assertTrue(hasattr(basemodel1, 'updated_at'))
        self.assertTrue(hasattr(basemodel1, 'id'))
        self.assertFalse(hasattr(basemodel1, 'destroyed_at'))

    def test_attrvalue(self):
        """Checks for attributes attributes type"""
        basemodel2 = BaseModel()
        self.assertTrue(type(basemodel2.id), str)
        self.assertTrue(type(basemodel2.created_at), str)
        self.asserTrue(type(basemodel2.updated_at), str)
