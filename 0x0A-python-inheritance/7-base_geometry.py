#!/usr/bin/python3

"""Class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises Exception

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that raises TypeError and ValueError

        Args:
            name (str): name
            value (int): value

        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))