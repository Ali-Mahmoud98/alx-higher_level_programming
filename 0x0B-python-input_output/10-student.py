#!/usr/bin/python3
"""Defines Class Student"""


class Student:
    """Student Class"""
    def __init__(self, first_name, last_name, age):
        """Initialization Method

        Args:
            first_name (str): student first name
            last_name (str): student last name
            age (int): student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        Returns:
            str : dictionary representation of Object.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
