#!/usr/bin/python3
""" This Module contains a function that loads
    a JSON representation into an object """
import json


def load_from_json_file(filename):
    """ This function converts 'my_obj' into a
        JSON representation and writes it to a file """
    with open(filename, 'r', encoding="utf-8") as f:
        json.load(f)
