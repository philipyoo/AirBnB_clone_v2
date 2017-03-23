import unittest
import os
from datetime import datetime
from models import *
from console import HBNBCommand


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE', '') == "db", "db")
class Test_BaseModel(unittest.TestCase):
    """
    Test the base model class
    """

    def setUp(self):
        self.cli = HBNBCommand()
        self.model1 = BaseModel()

        test_args = {'created_at': datetime(2017, 2, 11, 2, 6, 55, 258849),
                     'updated_at': datetime(2017, 2, 11, 2, 6, 55, 258966),
                     'id': '46458416-e5d5-4985-aa48-a2b369d03d2a',
                     'name': 'model1'}
        self.model2 = BaseModel(test_args)
        self.model2.save()

    def tearDown(self):
        self.cli.do_destroy("BaseModel 46458416-e5d5-4985-aa48-a2b369d03d2a")

    def test_instantiation(self):
        self.assertIsInstance(self.model1, BaseModel)
        self.assertTrue(hasattr(self.model1, "created_at"))
        self.assertTrue(hasattr(self.model1, "id"))
        self.assertTrue(hasattr(self.model1, "updated_at"))

    def test_reinstantiation(self):
        self.assertIsInstance(self.model2, BaseModel)
        self.assertEqual(self.model2.id,
                         '46458416-e5d5-4985-aa48-a2b369d03d2a')
        self.assertEqual(self.model2.created_at,
                         datetime(2017, 2, 11, 2, 6, 55, 258849))

    def test_save(self):
        old_time = self.model2.updated_at
        self.model2.save()
        self.assertNotEqual(old_time, self.model2.updated_at)

    def test_to_json(self):
        jsonified = self.model2.to_json()
        self.assertNotEqual(self.model2.__dict__, jsonified)
        self.assertNotIsInstance(jsonified["created_at"], datetime)
        self.assertNotIsInstance(jsonified["updated_at"], datetime)
        self.assertEqual(jsonified["created_at"], '2017-02-11 02:06:55.258849')
        self.assertTrue(hasattr(jsonified, "__class__"))
        self.assertEqual(jsonified["__class__"], "BaseModel")

    def test_to_json_no_sa_instance_state(self):
        jsonified = self.model2.to_json()
        self.assertFalse(hasattr(jsonified, "_sa_instance_state"))

if __name__ == "__main__":
    unittest.main()
