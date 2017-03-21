import unittest
from datetime import datetime
from models import *
from console import HBNBCommand


class Test_UserModel(unittest.TestCase):
    """
    Test the user model class
    """

    def setUp(self):
        self.cli = HBNBCommand()
        self.model = User()
        self.model.save()

    def tearDown(self):
        self.cli.do_destroy("User " + self.model.id)

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "__tablename__"))
        self.assertEqual(self.model.__tablename__, "users")
        self.assertTrue(hasattr(self.model, "email"))
        self.assertTrue(hasattr(self.model, "password"))
        self.assertTrue(hasattr(self.model, "first_name"))
        self.assertTrue(hasattr(self.model, "last_name"))


if __name__ == "__main__":
    unittest.main()
