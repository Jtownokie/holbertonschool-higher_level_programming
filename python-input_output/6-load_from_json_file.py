#!/usr/bin/python3
""" This Module contains a function that loads
    a JSON representation into an object """
import json


def load_from_json_file(filename):
    """ This function converts a JSON representation
        into an object """
    with open(filename, 'r', encoding="utf-8") as f:
        new_object = json.load(f)
    return new_object
