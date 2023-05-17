#!/usr/bin/python3
def uniq_add(my_list=[]):
    x = set()
    y = 0
    for y in my_list:
        x.add(y)
    y = sum(x)
    return y
