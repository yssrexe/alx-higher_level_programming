#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return None
    i = len(sentence)
    first_char = sentence[0]
    return i, first_char
