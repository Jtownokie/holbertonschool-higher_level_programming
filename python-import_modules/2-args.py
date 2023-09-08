#!/usr/bin/python3

from sys import argv as argv

if __name__ == "__main__":
    argc = len(argv) - 1
    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:\n1: {}".format(argc, argv[1]))
    elif argc > 1:
        print("{} arguments:")
        for i in range(1, argc + 1):
            print("{}: {}".format(i, argv[i]))
