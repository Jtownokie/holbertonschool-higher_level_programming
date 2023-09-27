#!/usr/bin/python3
""" This module contains a script that adds all arguments
    to a list and then saves them to a file """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":

    try:
        arg_list = load_from_json_file("add_item.json")
    except Exception:
        arg_list = []

    for arg in sys.argv:
        if arg is sys.argv[0]:
            continue
        else:
            arg_list.append(arg)

    save_to_json_file(arg_list, "add_item.json")
