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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """The height setter function

        Args:
            value (int): The value to be assigned to the height.

        Raises:
            TypeError: If the value to be assigned to height is not an int.
            ValueError: If the value to be assigned to height <= 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """The width setter function

        Args:
            value (int): The value to be assigned to the width.

        Raises:
            TypeError: If the value to be assigned to width is not an int.
            ValueError: If the value to be assigned to the width <= 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """Gets the x coordinate of the Rectangle.

        Returns:
            int: The x coordinate of the Rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """The x coordinate setter function

        Args:
            value (int): The value to be assigned to the x coordinate.

        Raises:
            TypeError: If the value to be assigned
                        to x coordinate is not an int.
            ValueError: If the value to be assigned to the x coordinate < 0.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y coordinate of the Rectangle.

        Returns:
            int: The y coordinate of the Rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """The y coordinate setter function

        Args:
            value (int): The value to be assigned to the y coordinate.

        Raises:
            TypeError: If the value to be assigned
                        to y coordinate is not an int.
            ValueError: If the value to be assigned to the y coordinate < 0.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Method calculates area.

        Returns:
            int: area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """Method that prints in stdout the
        Rectangle instance with the character #
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        print("\n" * self.y, end='')
        for i in range(self.height):
            print("{}{}".format(self.x * " ", self.width * "#"))

    def __str__(self):
        """Prints string representation of the rectangle.

        Returns:
            str: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Method that updates the Rectangle attribute values.

        Args:
            *args (ints): New attribute values.
                - id-> arg1
                - width-> arg2
                - height-> arg3
                - x-> arg4
                - y-> arg5
            **kwargs (dict): New key/value pairs of attributes.
        """
        for key, value in enumerate(args):
            if key == 0:
                self.id = value
            elif key == 1:
                self.width = value
            elif key == 2:
                self.height = value
            elif key == 3:
                self.x = value
            elif key == 4:
                self.y = value

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "width":
                self.width = value
            elif key == "height":
                self.height = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value

    def to_dictionary(self):
        """Method that returns the dictionary representation of a Rectangle.

        Returns:
            dict: representation of a Rectangle.
        """
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
