#!/usr/bin/python3
"""
4-from_json_string.py
Prototype:
def from_json_string(my_str):
"""


def from_json_string(my_str):
    """function that returns an object"""
    from json import loads
    return loads(my_str)
