#!/usr/bin/python3
"""
2-append_write.py
Prototype:
def append_write(filename="", text=""):
"""


def append_write(filename="", text=""):
    """def append_write"""
    with open(filename, "a", encoding="UTF-8") as f:
        st = f.write(text)
    return st
