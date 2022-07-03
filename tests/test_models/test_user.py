#!/usr/bin/python3
"""unittests for models/user.py"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Unittests"""

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_different_created_at(self):
        us1 = User()
        sleep(5)
        us2 = User()
        self.assertLess(us1.created_at, us2.created_at)

    def test_two_users_different_updated_at(self):
        us1 = User()
        sleep(3)
        us2 = User()
        self.assertLess(us1.updated_at, us2.updated_at)


if __name__ == "__main__":
    unittest.main()
