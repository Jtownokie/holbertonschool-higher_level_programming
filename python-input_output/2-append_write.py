#!/usr/bin/python3
""" This Module contains a function that appends to a file """


def append_write(filename="", text=""):
    """ This function opens and appends to a file """
    with open(filename, 'r+', encoding="utf-8") as f:
        charsprinted = f.write(text)

    return charsprinted
