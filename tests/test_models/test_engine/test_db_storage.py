import unittest
import os.path
import os
from datetime import datetime
from models.engine.db_storage import DBStorage
from models import *
from console import HBNBCommand


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE', '') != "db", "db")
class Test_DBStorage(unittest.TestCase):
    """
    Test the db storage class
    """

    def setUp(self):
        self.cli = HBNBCommand()
        self.store = DBStorage()

        test_args = {'updated_at': datetime(2017, 2, 12, 00, 31, 53, 331997),
                     'id': 'f519fb40-1f5c-458b-945c-2ee8eaaf4900',
                     'created_at': datetime(2017, 2, 12, 00, 31, 53, 331900),
                     'name': 'wifi'}
        self.model = Amenity(test_args)

    def test_init(self):
        self.assertNotEqual(self.store._DBStorage__engine, None)
        self.assertEqual(self.store._DBStorage__session, None)

    def test_all(self):
        self.store.reload()

        total = len(self.store.all())
        self.model.save()
        self.assertEqual(total + 1, len(self.store.all()))

        self.cli.do_create('User email="some@gmail.com" password="hello"')
        self.assertEqual(total + 2, len(self.store.all()))

    def test_all_class_specified(self):
        self.store.reload()

        total = len(self.store.all("Amenity"))
        self.model.save()
        self.assertEqual(total + 1, len(self.store.all("Amenity")))

        self.cli.do_create('Amenity name="bathroom"')
        self.assertEqual(total + 2, len(self.store.all("Amenity")))

    def test_all_invalid_class(self):
        self.store.reload()

        total = len(self.store.all())
        storage = self.store.all("Dog")

        self.assertTrue(storage == None)
        self.assertEqual(total, len(self.store.all()))

    def test_new(self):
        pass

    def test_save(self):
        pass

    def test_reload(self):
        self.store.reload()
        self.assertNotEqual(self.store._DBStorage__session, None)


if __name__ == "__main__":
    unittest.main()
