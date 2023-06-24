#!/usr/bin/python3
'''Function that returns an object (Python data structure)
    represented by a JSON string:'''


import json


def from_json_string(my_str):
    '''Converts a JSON string into its corresponding Python data structure.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The Python data structure represented by the JSON string.
    '''
    return json.loads(my_str)
