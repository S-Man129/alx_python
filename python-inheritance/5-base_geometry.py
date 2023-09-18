#!/usr/bin/python3
""" class BaseGeometry """


class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """ Method area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method integer validator """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        
    def __init_subclass__(cls):
        cls.__init_subclass__ = lambda *args, **kwargs: None

    def __dir__(self):
        # Get the default list of attributes and methods
        default_dir = super().__dir__()

        # Exclude '__init_subclass__' if it's in the default_dir
        if '__init_subclass__' in default_dir:
            default_dir.remove('__init_subclass__')

        return default_dir