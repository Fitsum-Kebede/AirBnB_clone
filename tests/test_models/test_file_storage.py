#!/usr/bin/python3
"""This module defines unit test for FileStorage class"""
import unittest
import json
import os
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class Test_FileStorage(unittest.TestCase):
    """ test for implementing the FileStorage class and integrating
    it with the existing classes
    """
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

    def tearDown(self):
        all_objs = list(storage.all().keys())
        for obj_id in all_objs:
            del storage._FileStorage__objects[obj_id]
            storage.save()

    def test_Initialization_and_Reload_empty_file(self):
        """Test the reload method to ensure that it correctly loads the JSON
        file into the __objects dictionary.
        """
        with open(self.temp_file_path, "w", encoding="utf-8") as file:
            json.dump("", file)
        s_instance = FileStorage()
        s_instance._FileStorage__file_path = self.temp_file_path
        s_instance.reload()
        return_value = s_instance.all()
        self.assertEqual(return_value, {})
        self.assertEqual(type(return_value), dict)

    def test_all_empty_store(self):
        store_instance = FileStorage()
        stored = store_instance.all()
        self.assertDictEqual(stored, {})

    def test_all_specific_instances(self):
        store_instance = FileStorage()
        instance1 = BaseModel()
        instance2 = BaseModel()
        store_instance._FileStorage__objects["BaseModel."
                                             + instance1.id] = instance1
        store_instance._FileStorage__objects["BaseModel."
                                             + instance2.id] = instance2
        stored = store_instance.all()
        expected_keys = [
            "BaseModel." + instance1.id,
            "BaseModel." + instance2.id,
        ]
        self.assertListEqual(list(stored.keys()), expected_keys)

    def test_all_method(self):
        """Use the all method and verify that the returned dictionary
        matches the objects stored.
        """
        store_instance = FileStorage()
        for n in range(5):
            instance = BaseModel()
            key = "{}.{}".format(type(instance).__name__, instance.id)
            store_instance._FileStorage__objects[key] = instance
        stored = store_instance.all()
        self.assertDictEqual(stored, store_instance._FileStorage__objects)
        self.assertListEqual(list(stored.keys()),
                             list(store_instance._FileStorage__objects.keys()))

    def test_all_class_name_format(self):
        store_instance = FileStorage()
        instance = BaseModel()
        store_instance.new(instance)
        stored = store_instance.all()
        expected_key = "{}.{}".format(type(instance).__name__, instance.id)
        self.assertIn(expected_key, stored)

    def test_all_after_add_and_remove(self):
        store_instance = FileStorage()
        instance1 = BaseModel()
        instance2 = BaseModel()
        store_instance._FileStorage__objects[type(instance1).__name__ + "."
                                             + instance1.id] = instance1
        store_instance._FileStorage__objects[type(instance2).__name__ + "."
                                             + instance2.id] = instance2
        stored1 = store_instance.all()
        del store_instance._FileStorage__objects[type(instance1).__name__ + "."
                                                 + instance1.id]
        stored2 = store_instance.all()
        self.assertNotIn(type(instance1).__name__ + "." +
                         instance1.id, stored2)
        self.assertIn(type(instance2).__name__ + "." + instance2.id, stored2)
        self.assertDictEqual(stored1, stored2)

    def test_new_mothod(self):
        s_instance = FileStorage()
        my_list = []
        for n in range(5):
            instance = BaseModel()
            my_list.append("{}.{}".format(type(instance).__name__,
                                          instance.id))
            s_instance.new(instance)
        all_instances = s_instance.all()
        self.assertDictEqual(all_instances, s_instance._FileStorage__objects)
        self.assertSequenceEqual(list(all_instances.keys()), my_list)

    def test_new_adds_instance_to_objects(self):
        s_instance = FileStorage()
        instance = BaseModel()
        s_instance.new(instance)
        s = (s_instance._FileStorage__objects[type(instance).__name__
                                              + '.' + instance.id])
        self.assertEqual(instance, s)

    def test_new_updates_objects_dictionary(self):
        s_instance = FileStorage()
        instance = BaseModel()
        s_instance.new(instance)
        all_instances = s_instance.all()
        self.assertEqual(all_instances, s_instance._FileStorage__objects)

    def test_new_adds_correct_key(self):
        s_instance = FileStorage()
        instance = BaseModel()
        s_instance.new(instance)
        all_instances = s_instance.all()
        self.assertIn(instance.__class__.__name__
                      + '.' + instance.id, all_instances)

    def test_new_with_none_instance(self):
        s_instance = FileStorage()
        with self.assertRaises(AttributeError):
            s_instance.new(None)

    def test_new_with_existing_key(self):
        s_instance = FileStorage()
        instance1 = BaseModel()
        instance2 = BaseModel(id=instance1.id)
        s_instance.new(instance1)
        s_instance.new(instance2)
        self.assertNotEqual(instance1, instance2)

    def test_save_serializes_to_json_file(self):
        s_instance = FileStorage()
        instance1 = BaseModel()
        instance2 = BaseModel()
        instance3 = BaseModel()
        s_instance.new(instance1)
        s_instance.new(instance2)
        s_instance.new(instance3)
        s_instance.save()
        json_content = s_instance.all()
        self.assertIn(type(instance1).__name__ + "." + instance1.id,
                      json_content)
        self.assertIn(type(instance2).__name__ + "." + instance2.id,
                      json_content)
        self.assertIn(type(instance3).__name__ + "." + instance3.id,
                      json_content)

    def test_save_calls_storage_save(self):
        instance = BaseModel()
        instance.save()
        instance_key = "{}.{}".format(type(instance).__name__, instance.id)
        self.assertTrue(storage._FileStorage__objects.get(instance_key))

    def test_reload_updates_objects(self):
        instance = BaseModel()
        instance.save()
        instance_key = type(instance).__name__ + "." + instance.id
        storage.reload()
        self.assertIsInstance(storage._FileStorage__objects[instance_key],
                              BaseModel)

    def test_storage_variable(self):
        instance = BaseModel()


if __name__ == "__main__":
    unittest.main()
