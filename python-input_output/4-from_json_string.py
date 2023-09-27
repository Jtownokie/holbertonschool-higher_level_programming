#!/usr/bin/python3
""" This Module contains a function that returns
    a decoded JSON representation of an object """
import json


def from_json_string(my_str):
    """ This function converts 'my_str' into an object """
    return json.loads(my_str)
