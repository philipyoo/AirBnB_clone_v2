import unittest
import os.path
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import *
from console import HBNBCommand


class Test_FileStorage(unittest.TestCase):
    """
    Test the file storage class
    """

    def setUp(self):
        self.cli = HBNBCommand()
        self.store = FileStorage()

        test_args = {'updated_at': datetime(2017, 2, 12, 00, 31, 53, 331997),
                     'id': 'f519fb40-1f5c-458b-945c-2ee8eaaf4900',
                     'created_at': datetime(2017, 2, 12, 00, 31, 53, 331900)}
        self.model = BaseModel(test_args)

        self.test_len = 0
        if os.path.isfile("file.json"):
            self.test_len = len(self.store.all())

    def test_all(self):
        self.assertEqual(len(self.store.all()), self.test_len)

    def test_new(self):
        print(len(self.store.all()), self.test_len)
        self.assertEqual(len(self.store.all()), self.test_len)
        self.model.save()
        self.assertEqual(len(self.store.all()), self.test_len + 1)
        a = BaseModel()
        a.save()
        self.assertEqual(len(self.store.all()), self.test_len + 2)
        self.cli.do_destroy("BaseModel f519fb40-1f5c-458b-945c-2ee8eaaf4900")
        self.cli.do_destroy("BaseModel " + a.id)

    def test_save(self):
        self.test_len = len(self.store.all())
        a = BaseModel()
        a.save()
        self.assertEqual(len(self.store.all()), self.test_len + 1)
        b = User()
        self.assertNotEqual(len(self.store.all()), self.test_len + 2)
        b.save()
        self.assertEqual(len(self.store.all()), self.test_len + 2)
        self.cli.do_destroy("BaseModel " + a.id)
        self.cli.do_destroy("User " + b.id)

    def test_reload(self):
        pass

if __name__ == "__main__":
    unittest.main()
