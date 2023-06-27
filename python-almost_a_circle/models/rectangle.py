#!/usr/bin/python3
'''Define class Rectangle'''


from models.base import Base


class Rectangle(Base):
    '''Represent a class Rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Inicialize Rectangle

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int): x-coordinate of the rectangle's position
            y (int): y-coordinate of the rectangle's position
            id (int): Unique identifier
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Getter for width'''
        return self.width

    @width.setter
    def width(self, value):
        '''Setter for width'''
        self.__width = value

    @property
    def height(self):
        '''Getter for height'''
        return self.height

    @height.setter
    def height(self, value):
        '''Setter for height'''
        self.__height = value

    @property
    def x(self):
        '''Getter for x'''
        return self.x

    @x.setter
    def x(self, value):
        '''Setter for x'''
        self.__x = value

    @property
    def y(self):
        '''Getter for y'''
        return self.x

    @y.setter
    def y(self, value):
        '''Setter for y'''
        self.__y = value
