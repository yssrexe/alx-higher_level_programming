#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    for n in set(my_list):
        res += n
    return res
