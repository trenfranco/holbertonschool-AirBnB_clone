#!/usr/bin/python3
"""Unittests for models/base_model.py."""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """unitest basmodel"""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_different_created_at(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_attr(self):
        self.assertEqual(Amenity.name, "")

    def test_subclass(self):
        self.assertTrue(issubclass(Amenity, BaseModel))


if __name__ == '__main__':
    unittest.main()
