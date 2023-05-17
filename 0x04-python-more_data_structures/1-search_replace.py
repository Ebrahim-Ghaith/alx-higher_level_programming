#!/usr/bin/python3
def search_replace(my_list, search, replace):
    x = 0
    length_x = len(my_list) - 1
    result = my_list.copy()
    while x < length_x:
        if result[x] == search:
            result[x] = replace
        x += 1
    return result
