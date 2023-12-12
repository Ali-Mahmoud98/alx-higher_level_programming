#!/usr/bin/python3
"""This module defines the base model class."""
import json


class Base:
    """Base Class.

    Private Class attributes:
        __nb_object (int): Number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization Function.

        Args:
            id (int, optional): The identity of the new Base.
                                Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # static method def to_json_string(list_dictionaries): => @staticmethod
    @staticmethod
    def to_json_string(list_dictionaries):
        """Method that returns the JSON string
        representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    # cls is a convention used to refer to the
    # class itself in a method or a class method.
    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        fileName = cls.__name__ + ".json"
        with open(fileName, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))
