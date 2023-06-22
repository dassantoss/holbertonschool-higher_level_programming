#!/usr/bin/python3
def lookup(obj):
    """This function returns the list of available attributes and methods of an object
    
    Args:
        obj: The object to inspect
        
    Returns:
        Returns a list object
    """
    return dir(obj)
