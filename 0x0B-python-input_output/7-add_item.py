#!/usr/bin/python3
"""
7-add_item.py
script that adds all arguments to a Python list
then save them to a file
"""

from sys import argv
save_to_json = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json = __import__('6-load_from_json_file.py').load_from_json_file

filename = "add_item.json"

try:
    my_list = load_from_json(filename)
except FileNotFoundError:
    my_list = []

for i in range(1, len(argv)):
    my_list.append(argv[i])
save_to_json(my_list, filename)
