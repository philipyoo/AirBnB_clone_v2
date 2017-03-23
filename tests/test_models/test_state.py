import unittest
from datetime import datetime
from models import *
from console import HBNBCommand


class Test_StateModel(unittest.TestCase):
    """
    Test the state model class
    """

    def setUp(self):
        self.cli = HBNBCommand()
        self.model = State()

    def tearDown(self):
        self.cli.do_destroy("State " + self.model.id)

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "__tablename__"))
        self.assertEqual(self.model.__tablename__, "states")
        self.assertTrue(hasattr(self.model, "name"))


if __name__ == "__main__":
    unittest.main()
