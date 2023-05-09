#!/usr/bin/python3
x = 97
while x <= 122:
    if x == 101 or x == 113:
        print(end="")
    else:
        char = chr(x)
        print("{}".format(char), end="")
    x += 1
