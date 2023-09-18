# #!/usr/bin/python3
""" Empty class BaseGeometry """

class BaseGeometry:
    """ Empty class BaseGeometry """
    def __dir__(self):
        """ defining directory self """
        return [attr for attr in dir(self) if attr != '__init_subclass__']
