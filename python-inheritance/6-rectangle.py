#!/usr/bin/python3
"""Rectangle class Module"""
BaseGeometry = __import__("5-base_geometry").BaseGeometry

class NoInitSubclassMeta(type):
    def __init_subclass__(cls):
        cls.__init_subclass__ = lambda *args, **kwargs: None

    def __dir__(self):
        return [attr for attr in dir(self) if not attr == '__init_subclass__']

class Rectangle(BaseGeometry, metaclass=NoInitSubclassMeta):
    """Rectangle class"""
    def __init__(self, width, height):
        """Initilize rectangle method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
