#!/usr/bin/python3
"""defines class Square that inherits from Rectangle"""


Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """class for square that inherits from Rectangle
    with method for area"""
    def __init__(self, size):
        """initializes Square instance"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns area of square"""
        return (self.__size * self.__size)
    
    def __init_subclass__(cls):
        cls.__init_subclass__ = lambda *args, **kwargs: None

    def __dir__(self):
        # Get the default list of attributes and methods
        default_dir = super().__dir__()

        # Exclude '__init_subclass__' if it's in the default_dir
        if '__init_subclass__' in default_dir:
            default_dir.remove('__init_subclass__')

        return default_dir