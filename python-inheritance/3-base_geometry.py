#!/usr/bin/python3
"""BaseGeometry class Module"""

class BaseGeometryMeta(type):
    """BaseGeometryMeta class """
    def __init_subclass__(cls):
        cls.__init_subclass__ = lambda *args, **kwargs: None

    def __dir__(self):
        default_dir = super().__dir__()
        default_dir.remove('__init_subclass__')
        return default_dir

class BaseGeometry(metaclass=BaseGeometryMeta):
    """BaseGeometry class Module"""
    def __dir__(self):
        default_dir = super().__dir__()
        default_dir.remove('__init_subclass__')
        return default_dir
    pass




    # def __init_subclass__(cls):
    #     cls.__init_subclass__ = lambda *args, **kwargs: None

    # def __dir__(self):
    #     # Get the default list of attributes and methods
    #     default_dir = super().__dir__()

    #     # Exclude '__init_subclass__' if it's in the default_dir
    #     if '__init_subclass__' in default_dir:
    #         default_dir.remove('__init_subclass__')

    #     return default_dir