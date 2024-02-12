#!/usr/bin/python3
"""
0x08-python-more_classes
2-rectangle.py
Area and Perimeter
"""


class Rectangle:
    """class Rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """compute and return rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """compute and return rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2*(self.__height + self.__width)
