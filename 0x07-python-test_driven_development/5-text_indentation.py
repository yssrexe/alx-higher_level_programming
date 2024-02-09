#!/usr/bin/python3
"""
This is '5-text_indentation' module.
Functions:
    text_indentation(text)
"""


def text_indentation(text):
    """
    text with 2 new lines after each of these characters: ., ? and :

    args:
        text (str): given text
    return:
        None
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    first = index = 0
    size = len(text)
    while first < size:
        while text[index] == ' ':
            index += 1
            first += 1
        while first < size and text[first] not in '?:.':
            first += 1
        print(text[index:first+1], end="")
        if first != size:
            print("\n")
        first += 1
        index = first
