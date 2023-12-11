#!/usr/bin/python3
"""Module Defines a Rectangle class that inherits from Base class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle Initialization Function

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle
            x (int, optional): The x coordinate of the new Rectangle.
                                Defaults to 0.
            y (int, optional): The y coordinate of the new Rectangle.
                                Defaults to 0.
            id (int, optional): The identity of the new Rectangle.
                                Defaults to None.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
