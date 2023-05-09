#!/usr/bin/python3
def islower(c):
    """
    Check if character c is lowercase or not
    """
    ascii_val = ord(c)
    if ascii_val >= 97 and ascii_val <= 122:
        return True
    else:
        return False
