#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represents a Square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            position (tuple): The position of the new Square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the Square.

        Args:
            value (int): The new size of the Square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the Square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the Square.

        Args:
            value (tuple): The new position of the Square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If value contains non-positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the Square.

        Returns:
            int: The area of the Square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the Square with the character '#'."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
