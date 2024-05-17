#!/usr/bin/python3
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel

class TestConsole(unittest.TestCase):
    def setUp(self):
        """
        Set up method for the tests
        """
        self.cli = HBNBCommand()

    def test_do_create(self):
        """
        Test the do_create command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            self.assertNotEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_do_show(self):
        """
        Test the do_show command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.cli.onecmd("show BaseModel " + obj_id)
            self.assertNotEqual(f.getvalue().strip(), "** no instance found **")

    def test_do_destroy(self):
        """
        Test the do_destroy command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            f.seek(0)
            f.truncate(0)
            self.cli.onecmd("destroy BaseModel " + obj_id)
            self.cli.onecmd("show BaseModel " + obj_id)
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_do_all(self):
        """
        Test the do_all command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("all")
            self.assertNotEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_do_update(self):
        """
        Test the do_update command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.cli.onecmd("update BaseModel " + obj_id + " first_name John")
            self.cli.onecmd("show BaseModel " + obj_id)
            self.assertIn("'first_name': 'John'", f.getvalue().strip())

if __name__ == "__main__":
    unittest.main()
