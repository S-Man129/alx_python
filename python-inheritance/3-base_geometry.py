#!/usr/bin/python3
""" Empty class BaseGeometry """

class BaseGeometry:
    """ Empty class BaseGeometry """
    def __init_subclass__(cls):
        """ excluding __init_subclass__ """
        cls.__init_subclass__ = lambda *args, **kwargs: None