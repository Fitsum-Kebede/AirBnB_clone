#!/usr/bin/python3
import unittest
import os
from models.user import User
from models import storage
from datetime import datetime


class Test_User_class(unittest.TestCase):
    """Test_BaseModel class  definition for testing User class"""
    @classmethod
    def setUpClass(cls):
        cls.temp_file_path = "airbnb.json"
        with open(cls.temp_file_path, "w") as file:
            file.write('{}')
        storage._FileStorage__file_path = cls.temp_file_path

    @classmethod
    def tearDownClass(cls):
        all_objs = list(storage.all().keys())
        for obj_id in all_objs:
            del storage._FileStorage__objects[obj_id]
            storage.save()
        if os.path.exists(cls.temp_file_path):
            os.remove(cls.temp_file_path)

    def test_id_generation(self):
        """Tests for the uniqueness of instance id and its type"""
        instance1 = User()
        instance2 = User()
        self.assertNotEqual(instance1.id, instance2.id)
        self.assertIsInstance(instance1.id, str)

    def test_created_updated_at(self):
        """Tests for difference in time an instance is created and updated"""
        instance = User()
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertEqual(instance.created_at, instance.updated_at)
        instance.name = "Example"
        instance.save()
        self.assertNotEqual(instance.created_at, instance.updated_at)

    def test_str_method(self):
        """Tests for string representation of the User instance"""
        instance = User()
        expected_output = "[User] ({}) {}".format(instance.id,
                                                  instance.__dict__)
        self.assertEqual(str(instance), expected_output)

    def test_save_method(self):
        """Tests for updated time on each update of an instance"""
        instance = User()
        prev_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(prev_updated_at, instance.updated_at)

    def test_to_dict_method(self):
        """Tests to_dict instance method for expected attributes in
        the dictionary
        """
        instance = User()
        instance.name = "Example"
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertIn('__class__', instance_dict)
        self.assertEqual(instance_dict['__class__'], 'User')
        self.assertEqual(instance_dict['id'], instance.id)
        self.assertEqual(instance_dict['name'], "Example")

    def test_re_create_from_dict_A(self):
        """Tests for the re-creation of an instance from the its
        dictionary representation
        <class 'User'>->to_dict()-><class 'dict'> -><class 'User'>
        """
        instance = User()
        instance.name = "Example"
        instance_dict = instance.to_dict()
        new_instance = User(**instance_dict)
        self.assertIsInstance(new_instance, User)
        self.assertEqual(new_instance.id, instance.id)
        self.assertEqual(new_instance.name, "Example")
        self.assertEqual(str(type(new_instance.created_at)),
                         "<class 'datetime.datetime'>")
        self.assertEqual(str(type(new_instance.updated_at)),
                         "<class 'datetime.datetime'>")

    def test_re_create_from_dict_B(self):
        instance = User()
        instance.name = "Modify me"
        instance_dict = instance.to_dict()
        del instance_dict["__class__"]
        instance_dict["known_as"] = "new instance"
        new_instance = User(**instance_dict)
        self.assertEqual(new_instance.created_at, instance.created_at)
        self.assertEqual(new_instance.updated_at, instance.updated_at)
        self.assertEqual(new_instance.id, instance.id)
        self.assertEqual(new_instance.__class__, User)
        self.assertIsNot(new_instance, instance)

    def test_time_format(self):
        instance = User()
        datetime_format = instance.to_dict()["created_at"]
        parsed_datetime = datetime.strptime(datetime_format,
                                            "%Y-%m-%dT%H:%M:%S.%f")
        formatted_datetime = parsed_datetime.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(datetime_format, formatted_datetime)


if __name__ == '__main__':
    unittest.main()
