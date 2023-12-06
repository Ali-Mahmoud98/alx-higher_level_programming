#!/usr/bin/python3
"""Module Defines class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Drived class from Rectangle."""
    def __init__(self, size):
        """Square Initializer Function.

        Args:
            size (int): size of the square.
        """
        self.integer_validator("size", size)
        super.__init__(size, size)
        self.__size = size
