#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = 0
    y = len(my_list) - 1
    new_list=[]
    while y >= 0:
        new_list.append(my_list[y])
        y -= 1
    return new_list
