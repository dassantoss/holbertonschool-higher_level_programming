#!/usr/bin/python3
'''Function that appends a string at the end of a text file (UTF8)'''


def append_write(filename="", text=""):
    '''appends a string at the end of a text file (UTF8)
    Args:
        filename (file): file to write
        text (str): string
    Returns:
        the number of characters written'''
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
