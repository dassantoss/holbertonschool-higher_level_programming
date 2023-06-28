#!/usr/bin/python3
'''Define class base'''

import json


class Base:
    '''Represent a class base'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Inicialize Base

        Args:
            id (int): Unique identifier
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Method to_json_string
        Returns:
             The JSON string representation of list_dictionaries
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
