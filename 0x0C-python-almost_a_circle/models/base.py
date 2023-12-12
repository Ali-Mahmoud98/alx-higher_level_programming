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
