#!/usr/bin/python3
""" Class Rectangle """
BaseGeometry = __import__('5-base_geometry').BaseGeometry

class NoInitSubclassMeta(type):
    def __init_subclass__(cls):
        cls.__init_subclass__ = lambda *args, **kwargs: None

    def __dir__(self):
        default_dir = super().__dir__()
        default_dir.remove('__init_subclass__')
        return default_dir

class Rectangle(BaseGeometry, metaclass=NoInitSubclassMeta):
    """ Class Rectangle """
    def __init__(self, width, height):
        """ init method """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ return area """
        return self.__width * self.__height

    def __str__(self):
        """ __str__ method """
        return("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
