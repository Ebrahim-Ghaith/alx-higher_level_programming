#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    for x in my_list:
        if x >= max:
            max = x
        else:
            max = max
    return max
