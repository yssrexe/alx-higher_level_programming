#!/usr/bin/python3
"""
Write a class MyList that inherits from list:
Public instance method: def print_sorted(self)
You can assume that all the elements
"""


class MyList(list):
    """
    subclass that inherits from 'list' class
    """
    def print_sorted(self):
        """print sorted list in ascending order"""
        sort_list = sorted(self)
        print(sort_list)
