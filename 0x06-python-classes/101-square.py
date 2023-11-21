#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        self.position = position

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    @property
    def size(self):
        """GET/SET current size of the Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Update size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """GET/SET current size of the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for position"""
        if (not isinstance(value, tuple)
                or len(value) != 2 or
                not all(isinstance(num, int) for num in value)
                or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
        else:
            if self.__position[1] > 0:
                print("\n"*(self.__position[1] - 1))
            for i in range(self.__size):
                print(" "*self.__position[0], end='')
                print("#"*self.__size)

    def __str__(self):
        """Define the print() representation of a Square."""
        str = ""
        if self.__size > 0:
            str += "\n"*(self.__position[1])
        for i in range(0, self.__size):
            str += " "*self.__position[0] + "#"*self.__size + "\n"
        return (str[:-2])
