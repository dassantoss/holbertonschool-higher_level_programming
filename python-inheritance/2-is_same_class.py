#!/usr/bin/python3
'''Function that checks if an object belongs to a class or not'''


def is_same_class(obj, a_class):
    '''Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    '''
    return isinstance(obj, a_class)
