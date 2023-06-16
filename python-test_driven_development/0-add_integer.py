#!/usr/bin/python3
"""This module defines the add_integer function that adds two integers."""


def add_integer(a, b=98):
    """Adds two integers and returns the result.

    Args:
        a (int): The first integer.
        b (int, optional): The second integer. Defaults to 98.

    Returns:
        int: The addition of the two integers.

    Raises:
        TypeError: If a or b is not an integer or float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return (int(a) + int(b))
