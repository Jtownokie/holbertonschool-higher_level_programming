#!/usr/bin/python3
""" This Module contains a function that writes
    an object to a text file using JSON representation """
import json


def save_to_json_file(my_obj, filename):
    """ This function converts 'my_obj' into a
        JSON representation and writes it to a file """
    with open(filename, 'w+', encoding="utf-8") as f:
        json.dump(my_obj, f)
