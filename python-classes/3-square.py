#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represents a Square."""
    pass

    def __init__(self, size=0):
        """Inicialized a new Square.

        Args:
            size (int): The size of the new Square.
        """
        self.__size = size
        self.__validate_size()

    def __validate_size(self):
        """Validate the size attribute.

        Raises:
            TypeError: if the size is not integer.
            TypeValue: if the size is less than 0.
        """
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate the current square area.

        Returns:
            int: The are of Square."""

        return self.__size * self.__size
