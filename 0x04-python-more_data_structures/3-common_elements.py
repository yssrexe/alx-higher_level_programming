#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = []
    for s1 in set_1:
        for s2 in set_2:
            if s1 == s2:
                new_list = s1
    return new_list
