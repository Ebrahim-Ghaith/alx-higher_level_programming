#!/usr/bin/python3
def no_c(my_string):
    y = ""
    for x in my_string:
        if x != 'c' and x != 'C':
            y += x
    return y
