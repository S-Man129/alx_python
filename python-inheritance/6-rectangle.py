#!/usr/bin/python3
""" Class Rectangle """

class BaseGeometryMeta(type):
    def __init_subclass__(cls):
        cls.__init_subclass__ = lambda *args, **kwargs: None

class BaseGeometry(metaclass=BaseGeometryMeta):
    def __dir__(self):
        default_dir = super().__dir__()
        default_dir.remove('__init_subclass__')
        return default_dir

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height

