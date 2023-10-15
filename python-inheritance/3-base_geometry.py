#!/usr/bin/python3
"""BaseGeometry class Module"""

class BaseGeometryMeta(type):
    """ BaseGeometry Empty class"""
    def __init_subclass__(cls):
        pass

class BaseGeometry(metaclass=BaseGeometryMeta):
    """ BaseGeometry Empty class"""
    pass