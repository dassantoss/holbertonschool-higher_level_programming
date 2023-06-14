#!/usr/bin/python3
"""Define class Square."""


class Square:
    """Represents a Square."""

    def __init__(self, size=0):
        """Inicialized a new Square.

        Args:
            size (int): The size of new Square (default is 0)
        """
        self.__size = size

    @property
    def size(self):
        """Get the size of the Square.

        Returns:
            int: The size of the Square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the Square

        Args:
            value (int): The new size value.

        Reises:
            TyperError: if the size is not integer.
            ValueError: if the size is less that 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the are of the Scuare

        Returns:
            int: The area of the Scuare
        """
        return self.__size * self.__size
