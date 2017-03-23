import unittest
from datetime import datetime
from models import *
from console import HBNBCommand


class Test_PlaceModel(unittest.TestCase):
    """
    Test the place model class
    """

    def setUp(self):
        self.cli = HBNBCommand()
        self.model = Place()

    def tearDown(self):
        self.cli.do_destroy("Place " + self.model.id)

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "__tablename__"))
        self.assertEqual(self.model.__tablename__, "places")
        self.assertTrue(hasattr(self.model, "city_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "name"))
        self.assertTrue(hasattr(self.model, "description"))
        self.assertTrue(hasattr(self.model, "number_rooms"))
        self.assertTrue(hasattr(self.model, "number_bathrooms"))
        self.assertTrue(hasattr(self.model, "max_guest"))
        self.assertTrue(hasattr(self.model, "price_by_night"))
        self.assertTrue(hasattr(self.model, "latitude"))
        self.assertTrue(hasattr(self.model, "longitude"))
        self.assertTrue(hasattr(self.model, "amenities"))


if __name__ == "__main__":
    unittest.main()
