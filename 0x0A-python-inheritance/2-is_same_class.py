#!/usr/bin/python3
"""
Prototype: def is_same_class(obj, a_class):
obj - class
return true or false
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of the class
    """
    return obj.__class__ is a_class
