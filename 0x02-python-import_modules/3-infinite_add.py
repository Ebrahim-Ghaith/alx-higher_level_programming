#!/usr/bin/python3
import sys
if __name__ == "__main__":
    x = 0
    arguments_count = len(sys.argv) - 1
    arguments = sys.argv[1:]
    for arg in arguments:
        x += int(arg)
    print("{}".format(x))
