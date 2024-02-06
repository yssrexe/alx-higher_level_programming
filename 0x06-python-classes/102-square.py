#!/usr/bin/python3

"""
This module defines a class and functions related to squares.
"""


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """
        Initializes a Square object with the specified size.

        Args:
            size: The size (length of a side) of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def __eq__(self, other):
        """
        Check if the square is equal to another square.

        Args:
            other: Another square object to compare with.

        Returns:
            bool: True if the area of the square is equal
            to the area of the other square, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Check if the square is not equal to another square.

        Args:
            other: Another square object to compare with.

        Returns:
            bool: True if the area of the square is not equal
            to the area of the other square, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Check if the square is less than another square.

        Args:
            other: Another square object to compare with.

        Returns:
            bool: True if the area of the square is less than
            the area of the other square, False otherwise.
        """
        return self.area() < other.area()

    def __gt__(self, other):
        """
        Check if the square is greater than another square.

        Args:
            other: Another square object to compare with.

        Returns:
            bool: True if the area of the square is greater than
            the area of the other square, False otherwise.
        """
        return self.area() > other.area()

    def __le__(self, other):
        """
        Check if the square is less than or equal to another square.

        Args:
            other: Another square object to compare with.

        Returns:
            bool: True if the area of the square is less than or equal
            to the area of the other square, False otherwise.
        """
        return self.area() <= other.area()

    def __ge__(self, other):
        """
        Check if the square is greater than or equal to another square.

        Args:
            other: Another square object to compare with.

        Returns:
            bool: True if the area of the square is greater than or equal
            to the area of the other square, False otherwise.
        """
        return self.area() >= other.area()
