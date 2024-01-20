#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = [element for element in my_list]
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        new_list[idx] = element
        return new_list
