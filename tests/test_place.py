#!/usr/bin/python3
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """
    Unit tests for the Place class defined
    """

    def test_create_place(self):
        """
        Creation of a place instance test
        """
        place = Place()
        self.assertEqual(place.__class__.__name__, "Place")
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])
