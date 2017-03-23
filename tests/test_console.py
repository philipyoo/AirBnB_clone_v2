import unittest
import sys
import io
from contextlib import contextmanager
from models import *
from datetime import datetime
from console import HBNBCommand


@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class Test_Console(unittest.TestCase):
    """
    Test the console
    """

    def setUp(self):
        self.cli = HBNBCommand()

        test_args = {'updated_at': datetime(2017, 2, 11, 23, 48, 34, 339879),
                     'id': 'd3da85f2-499c-43cb-b33d-3d7935bc808c',
                     'created_at': datetime(2017, 2, 11, 23, 48, 34, 339743),
                     'name': 'Test'}
        self.model = Amenity(test_args)
        self.model.save()

        self.creations = []

    def tearDown(self):
        self.cli.do_destroy("Amenity d3da85f2-499c-43cb-b33d-3d7935bc808c")

        for obj_id in self.creations:
            self.cli.do_destroy("Amenity " + obj_id)

    def test_quit(self):
        with self.assertRaises(SystemExit):
            self.cli.do_quit(self.cli)

    def test_show_correct(self):
        with captured_output() as (out, err):
            self.cli.do_show("Amenity d3da85f2-499c-43cb-b33d-3d7935bc808c")
        output = out.getvalue().strip()
        self.assertFalse("2017, 2, 11, 23, 48, 34, 339879" in output)
        self.assertTrue('2017, 2, 11, 23, 48, 34, 339743' in output)

    def test_show_error_no_args(self):
        with captured_output() as (out, err):
            self.cli.do_show('')
        output = out.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_show_error_missing_arg(self):
        with captured_output() as (out, err):
            self.cli.do_show("Amenity")
        output = out.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_show_error_invalid_class(self):
        with captured_output() as (out, err):
            self.cli.do_show("Human 1234-5678-9101")
        output = out.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_create_correct(self):
        with captured_output() as (out, err):
            self.cli.do_create('')
        output = out.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

        with captured_output() as (out, err):
            self.cli.do_create('Amenity name="Wifi"')
        output = out.getvalue().strip()
        self.creations.append(output)

        with captured_output() as (out, err):
            self.cli.do_show("Amenity {}".format(output))
        output2 = out.getvalue().strip()
        self.assertTrue(output in output2)

    def test_create_correct_with_extra_args(self):
        test_input = """Place city_id="0001" user_id="0001"
        name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10
        price_by_night=300 latitude=37.773972 longitude=-122.431297
        id="f519fb40-1f5c-458b-945c-2ee8eaaf4900" """

        with captured_output() as (out, err):
            self.cli.do_create(test_input)
        output = out.getvalue().strip()
        self.assertEqual(output, "f519fb40-1f5c-458b-945c-2ee8eaaf4900")
        self.cli.do_destroy("Place f519fb40-1f5c-458b-945c-2ee8eaaf4900")

    def test_destroy_correct(self):
        test_args = {'updated_at': datetime(2017, 2, 12, 00, 31, 53, 331997),
                     'id': 'f519fb40-1f5c-458b-945c-2ee8eaaf4900',
                     'created_at': datetime(2017, 2, 12, 00, 31, 53, 331900),
                     'name': 'Coffee'}
        testmodel = Amenity(test_args)
        testmodel.save()
        self.cli.do_destroy("Amenity " + testmodel.id)

        with captured_output() as (out, err):
            self.cli.do_show("Amenity f519fb40-1f5c-458b-945c-2ee8eaaf4900")
        output = out.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_destroy_error_missing_id(self):
        with captured_output() as (out, err):
            self.cli.do_destroy("Amenity")
        output = out.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_destroy_error_invalid_class(self):
        with captured_output() as (out, err):
            self.cli.do_destroy("Human d3da85f2-499c-43cb-b33d-3d7935bc808c")
        output = out.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_error_invalid_id(self):
        with captured_output() as (out, err):
            self.cli.do_destroy("Amenity " +
                                "f519fb40-1f5c-458b-945c-2ee8eaaf4900")
        output = out.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_all_correct(self):
        test_args = {'updated_at': datetime(2017, 2, 12, 00, 31, 53, 331997),
                     'id': 'f519fb40-1f5c-458b-945c-2ee8eaaf4900',
                     'created_at': datetime(2017, 2, 12, 00, 31, 53, 331900),
                     'name': 'fridge'}
        testmodel = Amenity(test_args)
        testmodel.save()
        self.creations.append(testmodel.id)

        with captured_output() as (out, err):
            self.cli.do_all("")
        output = out.getvalue().strip()
        self.assertTrue("d3da85f2-499c-43cb-b33d-3d7935bc808c" in output)
        self.assertTrue("f519fb40-1f5c-458b-945c-2ee8eaaf4900" in output)
        self.assertFalse("123-456-abc" in output)

    def test_all_correct_with_class(self):
        with captured_output() as (out, err):
            self.cli.do_all("Amenity")
        output = out.getvalue().strip()
        self.assertTrue(len(output) > 0)
        self.assertTrue("d3da85f2-499c-43cb-b33d-3d7935bc808c" in output)

    def test_all_error_invalid_class(self):
        with captured_output() as (out, err):
            self.cli.do_all("Human")
        output = out.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_update_correct(self):
        with captured_output() as (out, err):
            self.cli.do_update("Amenity " +
                               "d3da85f2-499c-43cb-b33d-3d7935bc808c name Bay")
        output = out.getvalue().strip()
        self.assertEqual(output, '')

        with captured_output() as (out, err):
            self.cli.do_show("Amenity d3da85f2-499c-43cb-b33d-3d7935bc808c")
        output = out.getvalue().strip()
        self.assertTrue("Bay" in output)
        self.assertFalse("Test" in output)

    def test_update_error_invalid_id(self):
        with captured_output() as (out, err):
            self.cli.do_update("Amenity 123-456-abc name Cat")
        output = out.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_update_error_invalid_class(self):
        with captured_output() as (out, err):
            self.cli.do_update("Human " +
                               "d3da85f2-499c-43cb-b33d-3d7935bc808c name Cat")
        output = out.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_update_error_missing_value(self):
        with captured_output() as (out, err):
            self.cli.do_update("Amenity " +
                               "d3da85f2-499c-43cb-b33d-3d7935bc808c name")
        output = out.getvalue().strip()
        self.assertEqual(output, "** value missing **")

if __name__ == "__main__":
    unittest.main()
