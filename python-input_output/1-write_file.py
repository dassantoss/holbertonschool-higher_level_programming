#!/usr/bin/python3
'''Function that write a string'''


def write_file(filename="", text=""):
    '''Writes a string to a text file (UTF8)
    Args:
        filename (file): file to write
        text (str): string
    Returns:
        the number of characters written'''
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
