#!/usr/bin/python3
""" This Module contains a function that writes to a file """


def write_file(filename="", text=""):
    """ This function opens and writes to a file """
    with open(filename, 'w+', encoding="utf-8") as f:
        charsprinted = f.write(text)

    return charsprinted

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
