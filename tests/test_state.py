#!/usr/bin/python3
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """
    State class unit tests defined
    """

    def test_create_state(self):
        """
        Creation of a state instance tested
        """
        state = State()
        self.assertEqual(state.__class__.__name__, "State")
        self.assertEqual(state.name, "")
