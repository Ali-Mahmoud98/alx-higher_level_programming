#!/usr/bin/python3
"""Defines Rectangle Class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle drived from BaseGeometry."""

    def __init__(self, width, height):
        """Constructor Function

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String Representation of Rectangle

        Returns:
            Rectangle description: [Rectangle] <width>/<height>
        """
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width, self.__height)
