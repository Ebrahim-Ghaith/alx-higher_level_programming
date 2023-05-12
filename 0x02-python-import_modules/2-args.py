#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = 0
    n = len(sys.argv) - 1
    if n:
        if n == 1:
            print("{} argument".format(n))
        else:
            print("{} arguments".format(n))
        while x < n:
            print("{}: {}".format(n, sys.argv[x + 1]))
            x += 1
    else:
        print("0 arguments")
