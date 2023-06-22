#!/usr/bin/python3
'''Define class BaseGeometry'''


class BaseGeometry:
    '''Represent class BaseGeometry'''
    pass

    def area(self):
        '''Method not implemented

        Raises:
            Exeption area() is not implemented
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validate a parameter as an integer.
        Args:
            name (str): the name of parameter
            value (int): The parameter to validate
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
