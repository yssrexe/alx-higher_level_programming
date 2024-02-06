#!/usr/bin/python3

class Square:
    """class Square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """return the square area"""
        return (self.__size)**2
    
    def my_print(self):
        """" print square using '#' """

        if self.__size == 0:
            print("")
            return

        for i in range(0, self.__position[1]):
            print("")

        for j in range(0, self.__size):
            for sp in range(0, self.__position[0]):
                print(" ", end="")
            for i in range(0, self.__size):
                print("#", end="")
            print("")
