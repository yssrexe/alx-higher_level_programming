#!/usr/bin/python3
def multiple_returns(sentence):
    i = len(sentence)
    if sentence == "":
        return i, None
    else:
        first_char = sentence[0]
        return i, first_char
