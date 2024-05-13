#!/usr/bin/python3
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """
    Unit tests defined for City class
    """

    def test_create_city(self):
        """
        Creation of a City instance tested.
        """
        city = City()
        self.assertEqual(city.__class__.__name__, "City")
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
