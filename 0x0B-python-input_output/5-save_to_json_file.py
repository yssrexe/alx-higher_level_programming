#!/usr/bin/python3
"""
5-save_to_json_file.py
prototype:
def save_to_json_file(my_obj, filename):
"""


def save_to_json_file(my_obj, filename):
    """function that writes an Object"""
    from json import dump
    with open(filename, "w", encoding="UTF-8") as f:
        dump(my_obj, f)
