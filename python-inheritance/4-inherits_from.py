#!/usr/bin/python3
'''Function inherits_from()'''


def inherits_from(obj, a_class):
    '''Check if an object is an instance of a class that inherited

    Args:
        obj (any): The object to check.
        a_class (type): The class to check for inheritance from.

    Returns:
        bool: Returns True or Flase
    '''
    return type(obj) != a_class and issubclass(type(obj), a_class)
