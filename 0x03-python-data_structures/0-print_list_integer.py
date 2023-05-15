#!/usr/bin/python3
def print_list_integer(my_list=[]):
    x = 0
    y = len(my_list)
    while x < y:
        print("{:d}".format(my_list[x]))
        x += 1
