#!/usr/bin/python3

def roman_to_int(roman_string):
    r_nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    if type(roman_string) is not str or roman_string is None:
        return 0
    if len(roman_string) == 1:
        return r_nums.get(roman_string)
    for i in range(len(roman_string)):
        if i + 1 == len(roman_string):
            total += r_nums.get(roman_string[i])
        elif r_nums.get(roman_string[i]) >= r_nums.get(roman_string[i + 1]):
            total += r_nums.get(roman_string[i])
        else:
            total -= r_nums.get(roman_string[i])
    return total
