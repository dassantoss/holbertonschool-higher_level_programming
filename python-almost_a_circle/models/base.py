#!/usr/bin/python3
'''Define class base'''

import json
import turtle


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

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string representation to a list of dictionaries.
        Args:
            json_string (str): Representing a list of dictionaries in JSON.
        Returns:
            list: A list of dictionaries representing the data from the JSON.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

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

    @classmethod
    def create(cls, **dictionary):
        '''Class method to create an instance with attributes already set
        Args:
            **dictionary: Double pointer to a dictionary
        Returns:
            Base: An instance with all attributes set
        '''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''Class method to load a list of instances from a JSON file
        Returns:
            list: A list of instances loaded from the file
        '''
        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r") as f:
                json_string = f.read()
        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(json_string)
        instances = [cls.create(**d) for d in list_dicts]

        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''Static method to draw Rectangles and Squares using the Turtle graphics module

        Args:
            list_rectangles (list): A list of Rectangle instances
            list_squares (list): A list of Square instances

        Returns:
            None
        '''
        # Create the Turtle screen
        screen = turtle.Screen()

        # Create a Turtle object
        t = turtle.Turtle()

        # Set the Turtle speed
        t.speed(2)

        # Draw Rectangles
        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            for _ in range(2):
                t.forward(rect.width)
                t.right(90)
                t.forward(rect.height)
                t.right(90)

        # Draw Squares
        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for _ in range(4):
                t.forward(square.size)
                t.right(90)

        # Exit on click
        turtle.exitonclick()
