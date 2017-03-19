import unittest
from datetime import datetime
from models import *
from console import HBNBCommand


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
        self.assertFalse(hasattr(self.model1, "updated_at"))

    def test_reinstantiation(self):
        self.assertIsInstance(self.model2, BaseModel)
        self.assertEqual(self.model2.id,
                         '46458416-e5d5-4985-aa48-a2b369d03d2a')
        self.assertEqual(self.model2.created_at,
                         datetime(2017, 2, 11, 2, 6, 55, 258849))

    def test_save(self):
        self.assertFalse(hasattr(self.model1, "updated_at"))
        self.model1.save()
        self.assertTrue(hasattr(self.model1, "updated_at"))
        old_time = self.model2.updated_at
        self.model2.save()
        self.assertNotEqual(old_time, self.model2.updated_at)
        self.cli.do_destroy("BaseModel " + self.model1.id)

    def test_to_json(self):
        jsonified = self.model2.to_json()
        self.assertNotEqual(self.model2.__dict__, jsonified)
        self.assertNotIsInstance(jsonified["created_at"], datetime)
        self.assertNotIsInstance(jsonified["updated_at"], datetime)
        self.assertEqual(jsonified["created_at"], '2017-02-11 02:06:55.258849')
        self.assertTrue(hasattr(jsonified, "__class__"))
        self.assertEqual(jsonified["__class__"], "BaseModel")

if __name__ == "__main__":
    unittest.main()
