#!/usr/bin/python3
"""Define class Square"""


class Square:
    """Represents a Square"""

    def __init__(self, size=0):
        """Inicialized a new Square

        Args:
            size (int): The size of the new Square (Default is 0)
        """
        self.__size = size

    @property
    def size(self):
        """Get the size of the Square

        Return:
            size (int): The size of the Square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the Square

        Args:
            value (int): The new size value of the Square

        Raises:
            TypeError: if the size is not a Integer
            ValueError: if the size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the Square.

        Returns:
            int: The area of the Square
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints in the stdout the Square with the char #"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
