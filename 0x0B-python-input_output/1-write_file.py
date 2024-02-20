#!/usr/bin/python3
"""
1-write_file.py
Prototype: 
def write_file(filename="", text=""):
"""
def write_file(filename="", text=""):
    """def write_file(filename="", text="")"""
    with open(filename, "w", encoding="UTF-8") as f:
        st = f.write(text)
    return st
