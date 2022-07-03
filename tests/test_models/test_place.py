#!/usr/bin/python3
"""unittests for models/place.py"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittests"""

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_subclass(self):
        self.assertTrue(issubclass(Place, BaseModel))


if __name__ == '__main__':
    unittest.main()
