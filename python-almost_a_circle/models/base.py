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
        '''Static method to convert a list of dictionaries to a JSON string
        Args:
            list_dictionaries (list): A list of dictionaries
        Returns:
            str: The JSON string representation of the list of dictionaries
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Class method to save a list of instances to a JSON file
        Args:
            list_objs (list): A list of instances
        Returns:
            None
        '''
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"

        list_dicts = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(list_dicts)

        with open(filename, "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string representation to a list of dictionaries.
        Args:
            json_string (str): A string representing a list of dictionaries in JSON format.
        Returns:
            list: A list of dictionaries representing the data from the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
