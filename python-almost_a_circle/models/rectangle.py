#!/usr/bin/python3
'''Define class Rectangle'''


from models.base import Base


class Rectangle(Base):
    '''Represents a rectangle, inherits from Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialize Rectangle

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int): x-coordinate of the rectangle's position
            y (int): y-coordinate of the rectangle's position
            id (int): Unique identifier
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''Getter for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for width'''
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        '''Getter for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for height'''
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        '''Getter for x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter for x'''
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        '''Getter for y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter for y'''
        self.validator("y", value)
        self.__y = value

    def area(self):
        '''Calcule the area value of the Rectangle
        Returns:
            the area value of the Rectangle
        '''
        return self.__width * self.__height

    def display(self):
        '''Prints in stdout the Rectangle'''
        for _ in range(self.height):
            print("#" * self.width)

    @staticmethod
    def validator(name, value):
        '''Validate if a value is an integer and positive
        Args:
            name (str): Name of the attribute
            value (int): Value of the attribute
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is not positive
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if name == "x" or name == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def __str__(self):
        '''Method __str__
        Returns:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)
