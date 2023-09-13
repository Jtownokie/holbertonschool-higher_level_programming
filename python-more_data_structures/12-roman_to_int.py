#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    if type(roman_string) is not str or roman_string is None:
        return 0
    if len(roman_string) == 1:
        return roman_nums.get(roman_string)
    for i in range(len(roman_string)):
        if i + 1 == len(roman_string):
            total += roman_nums.get(roman_string[i])
        elif roman_nums.get(roman_string[i]) >= roman_nums.get(roman_string[i + 1]):
            total += roman_nums.get(roman_string[i])
        else:
            total -= roman_nums.get(roman_string[i])
    return total
