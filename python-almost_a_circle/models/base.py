#!/usr/bin/python3
'''Define class base'''

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
