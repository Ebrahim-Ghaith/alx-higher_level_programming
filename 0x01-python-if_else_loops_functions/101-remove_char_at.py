#!/usr/bin/python3
def remove_char_at(str, n):
    """Return a copy of str with the character at position n removed."""
    # Check if n is a valid index
    if n < 0 or n >= len(str):
        return str
    # Build the result string by skipping the character at position n
    result = ""
    for i in range(len(str)):
        if i != n:
            result += str[i]
    return result
