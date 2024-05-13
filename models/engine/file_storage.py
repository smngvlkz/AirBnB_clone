#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """
    Serializes instances to a JSON file & deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists; otherwise do nothing).
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
                for k, v in objs.items():
                    cls_name = v['__class__']
                    cls = eval(cls_name)
                    self.__objects[k] = cls(**v)
