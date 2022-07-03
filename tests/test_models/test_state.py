#!/usr/bin/python3
"""Unittests for models/state.py"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Unittests"""

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_two_states_unique_ids(self):
        st1 = State()
        st2 = State()
        self.assertNotEqual(st1.id, st2.id)

    def test_two_states_different_updated_at(self):
        st1 = State()
        sleep(1)
        st2 = State()
        self.assertLess(st1.updated_at, st2.updated_at)

    def test_args_unused(self):
        st = State(None)
        self.assertNotIn(None, st.__dict__.values())


if __name__ == "__main__":
    unittest.main()
