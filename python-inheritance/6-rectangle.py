#!/usr/bin/python3
""" Class Rectangle """
BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle """
    def __init__(self, width, height):
        """ init method """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def __init_subclass__(cls):
        cls.__init_subclass__ = lambda *args, **kwargs: None

    def __dir__(self):
        # Get the default list of attributes and methods
        default_dir = super().__dir__()

        # Exclude '__init_subclass__' if it's in the default_dir
        if '__init_subclass__' in default_dir:
            default_dir.remove('__init_subclass__')

        return default_dir