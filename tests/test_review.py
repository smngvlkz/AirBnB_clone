#!/usr/bin/python3
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """
    Unit tests or Review Class defined
    """

    def test_create_review(self):
        """
        Creation of a review instance tested
        """
        review = Review()
        self.assertEqual(review.__class__.__name__, "Review")
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
