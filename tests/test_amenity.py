#!/usr/bin/python3
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """
    Unit tests for the Amenity class tested
    """

    def test_create_amenity(self):
        """
        Creation of an Amenity instance tested.
        """
        amenity = Amenity()
        self.assertEqual(amenity.__class__.__name__, "Amenity")
        self.assertEqual(amenity.name, "")
