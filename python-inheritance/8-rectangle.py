#!/usr/bin/python3
'''Define Rectangle class'''


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''Represent Rectangle class'''

    def __init__(self, width, height):
        '''Inicialized Module Rectangle
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        '''
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height
