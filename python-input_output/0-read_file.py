#!/usr/bin/python3
'''Function that reads a file'''


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.
    Args:
        filename (file): file to read
    Returns:
        none
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
