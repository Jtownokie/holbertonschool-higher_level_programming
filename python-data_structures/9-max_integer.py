#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    current_max = 0
    for i in range(0, len(my_list) - 1):
        if my_list[i] > current_max:
            current_max = my_list[i]
        else:
            continue
    
    return current_max
