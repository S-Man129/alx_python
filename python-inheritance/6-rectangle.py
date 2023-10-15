#!/usr/bin/python3
"""Rectangle class Module"""
BaseGeometry = __import__("5-base_geometry").BaseGeometry

class RectangleMeta(type):
    """Rectangle class"""
    def __init_subclass__(cls):
        cls.__init_subclass__ = lambda *args, **kwargs: None

class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Initilize rectangle method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    
    def __dir__(self):
        default_dir = super().__dir__()
        default_dir.remove('__init_subclass__')
        return default_dir
