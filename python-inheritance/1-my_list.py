#!/usr/bin/python3
'''Module: 1-mylist.py'''


class MyList(list):
    '''Represent class MyList, which Inherits from list'''

    def print_sorted(self):
        '''Function print_sorted prints the list sorted'''
        print(sorted(self))
