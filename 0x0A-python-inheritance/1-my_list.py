#!/usr/bin/python3
"""
Write a class MyList that inherits from list:
Public instance method: def print_sorted(self)
You can assume that all the elements
"""


class MyList(list):
    def print_sorted(self):
        """
        Prints the list in sorted order
        """
        sort_list = sorted(self)
        print(sort_list)
