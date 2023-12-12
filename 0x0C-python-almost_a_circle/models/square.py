#!/usr/bin/python3
"""This model defines Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Intialization of Square.
        This method called when instanciating instance of Rectangle.

        Args:
            size (int): The size of the new Rectangle.
            x (int, optional): The x coordinate of the new Square.
                                Defaults to 0.
            y (int, optional): The y coordinate of the new Square.
                                Defaults to 0.
            id (int, optional): The identity of the new Square.
                                Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Setting value to size.

        Args:
            value (int): the value to be assigned to size.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
