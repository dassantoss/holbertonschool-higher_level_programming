#!/usr/bin/python3
"""Define class Square"""


class Square:
    """Represents a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Inicialized the new Square

        Args:
            size (int): Size of the new Square (default 0)
            position (tupla): Position of the new Square (default (0,0))
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get the size of the Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the Square

        Args:
            value (int): The new Size of the Square

        Raises:
            TypeError: If the value is not integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the Square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the Square

        Args:
            value (tuple): The new position of the Square

        Raises:
            TypeError: If the value is not a Tuple of 2 positive integeres
            ValueError: If the value constains non-positive integers
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the char #"""
        if self.__size == 0:
            print()
        else:
            [print() for _ in range(0, self.__position[1])]
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
