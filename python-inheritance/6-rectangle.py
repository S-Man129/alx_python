#!/usr/bin/python3
""" Class Rectangle """
BaseGeometry = __import__('5-base_geometry').BaseGeometry

class BaseGeometry:
    def area(self):
        raise NotImplementedError("area() method not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)