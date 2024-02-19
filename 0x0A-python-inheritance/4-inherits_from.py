#!/usr/bin/python3
"""
4-inherits_from.py
Prototype:
def inherits_from(obj, a_class):
"""


def inherits_from(obj, a_class):
    """
    the object is an instance of a class that inherited
    """
    if isinstance(obj, type):
        return issubclass(obj, a_class)
    else:
        return any(inherits_from(base, a_class) for base in obj.__class__.__bases__)
