#!/usr/bin/python3
""" This Module contains a function that reads a file """


def read_file(filename=""):
    """ This Module opens and reads a file to stdout """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
