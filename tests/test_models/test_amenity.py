import unittest
from datetime import datetime
from models import *
from console import HBNBCommand


class Test_AmenityModel(unittest.TestCase):
    """
    Test the amenity model class
    """

    def setUp(self):
        self.cli = HBNBCommand()
        self.model = Amenity()
        self.model.save()

    def tearDown(self):
        self.cli.do_destroy("Amenity " + self.model.id)

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "__tablename__"))
        self.assertEqual(self.model.__tablename__, "amenities")
        self.assertTrue(hasattr(self.model, "name"))


if __name__ == "__main__":
    unittest.main()
