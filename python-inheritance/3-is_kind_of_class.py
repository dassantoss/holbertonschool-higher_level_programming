#!/usr/bin/python3
'''Function that checks if an class or inherit from'''


def is_kind_of_class(obj, a_class):
    '''Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        Returns True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class ; otherwise False.
    '''
    return isinstance(obj, a_class)
