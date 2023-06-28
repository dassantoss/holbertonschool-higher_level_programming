#!/usr/bin/python3
'''Define class Square'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''Represents a Square, inherits from Rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initialize Square

        Args:
            size (int): size of the square
            x (int): x-coordinate of the square's position
            y (int): y-coordinate of the square's position
            id (int): Unique identifier
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Getter for size'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter for size'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Update the Square
        Args:
            *args: No-keyword arguments
            **kwargs: Key-worded arguments
        '''
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        '''Method __str__
        Returns:
            [Square] (<id>) <x>/<y> - <size>
        '''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.size)
