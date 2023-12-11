#!/usr/bin/python3
"""This module defines the base model class."""


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
