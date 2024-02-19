#!/usr/bin/python3
"""
7-base_geometry.py
class:
BaseGeometry
"""


class BaseGeometry():
    """BaseGeometry class"""
    def area(self):
        """def area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """def integer_validator"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
