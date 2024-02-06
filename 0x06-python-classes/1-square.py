#!/usr/bin/python3

"""
This module defines a class and functions related to squares.
"""


class Square:
    """A class representing a square."""
    def __init__(self, size):
        """
        Initializes a Square object with the specified size.

        Args:
            size: The size (length of a side) of the square.
        """
        self.__size = size
