#!/usr/bin/python3

"""
This module defines a class and functions related to squares.
"""


class Square:
    """A class representing a square."""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object with the specified size.

        Args:
            size: The size (length of a side) of the square.
            position (tuple): The position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value: The new size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for the position attribute.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.

        Args:
            value (tuple): The new position to set, as a tuple of 2 ints.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print a square pattern of '#' characters."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Print a square pattern of '#' characters."""
        if self.__size == 0:
            return ""
        else:
            for _ in range(self.__position[1]):
                print()
            for i in range(self.__size):
                if i == self.__size - 1:
                    print(" " * self.__position[0] + "#" * self.__size, end="")
                    return ''
                else:
                    print(" " * self.__position[0] + "#" * self.__size)
