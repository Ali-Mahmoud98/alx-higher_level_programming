#!/usr/bin/python3

"""
Defines a Class Rectangle
"""


class Rectangle:
    """
    Rectangle class with hight and width attributes
    """
    def __init__(self, width=0, height=0):
        """
        initiate properties

        Args:
        width (int): Rectangles' width
        height (int): Rectangles' height
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0

        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        Print Rectangle using #

        Returns:
            str: formatted string
        """
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return ""

        for i in range(self.__height - 1):
            rect += "#"*self.__width + "\n"

        rect += "#"*self.__width
        return rect

    def __repr__(self):
        """
        Print expression for instantiating another Rectangle

        Returns:
            str: formatted string
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Destractor"""
        print("Bye rectangle...")
