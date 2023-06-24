#!/usr/bin/python3
'''Function that returns the JSON representation of an object (string)'''


import json


def to_json_string(my_obj):
    '''function that returns the JSON representation of an object (string)
    Returns:
        returns the JSON representation of an object (string):
    '''
    json_string = json.dumps(my_obj)
    return json_string
