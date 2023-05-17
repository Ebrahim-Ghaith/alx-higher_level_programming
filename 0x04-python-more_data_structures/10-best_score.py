#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    x = ""
    if a_dictionary is None:
        return None
    else:
        for key, value in a_dictionary.items():
            if value > max:
                max = value
                x = key
            else:
                continue
    return x
