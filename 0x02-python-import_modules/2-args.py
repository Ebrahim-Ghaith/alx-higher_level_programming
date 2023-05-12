#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments_count = len(sys.argv) - 1
    arguments = sys.argv[1:]

    print("{} {}{}{}".format(
    arguments_count,
    "argument" if arguments_count == 1 else "arguments",
    ":" if arguments_count > 0 else ".",
    "\n" if arguments_count > 0 else ""
),end="")

    for i, arg in enumerate(arguments):
        print("{}: {}".format(i + 1, arg))
