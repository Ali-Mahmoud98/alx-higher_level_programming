#!/usr/bin/python3
"""Defines BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry Class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that validates value.
        Args:
            name (string): name of the parameter.
            value (int): parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("must be greater than 0".format(name))
