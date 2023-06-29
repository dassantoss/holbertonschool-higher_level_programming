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
        '''Static method to_json_string
        Returns:
             The JSON string representation of list_dictionaries
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Method save_to_file writes the JSON string
        Args:
            cls: Class name
            list_objs:  List of instances
        '''
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = class_name + ".json"

        list_dicts = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(list_dicts)

        with open(filename, "w") as f:
            f.write(json_string)
