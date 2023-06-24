#!/usr/bin/python3
'''Function that reads a file'''


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.
    Returns none
    """
    script_path = __file__
    script_dir = script_path[:script_path.rfind('/') + 1]
    file_path = script_dir + filename
    with open(file_path, "r", encoding="utf-8") as file:
        print(file.read())
