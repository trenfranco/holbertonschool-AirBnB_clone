#!/usr/bin/python3

""" Unit tests Amenity class """

from models.amenity import Amenity
import unittest
from datetime import datetime
import os
import models


class TestAmenity(unittest.TestCase):
    """ Unit tests Amenity class """

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_two_amenities_unique_ids(self):
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)


if __name__ == '__main__':
    unittest.main()
