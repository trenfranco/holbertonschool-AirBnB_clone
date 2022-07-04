#!/usr/bin/python3
""""Unittests for models/review.py"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Unittests"""

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_two_reviews_different_updated_at(self):
        rv1 = Review()
        sleep(0.10)
        rv2 = Review()
        self.assertLess(rv1.updated_at, rv2.updated_at)


if __name__ == '__main__':
    unittest.main()
