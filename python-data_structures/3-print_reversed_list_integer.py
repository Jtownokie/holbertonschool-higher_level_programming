#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    my_list_copy = my_list.reverse()
    for item in my_list_copy:
        print("{:d}".format(item))
