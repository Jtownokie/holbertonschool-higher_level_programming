#!/usr/bin/python3
""" This Module contains a function that adds newlines in a string """


def text_indentation(text):
    """ This Function adds two newlines after every ., ?, and : """
    if type(text) is not str:
        raise TypeError('text must be a string')

    text1 = text.replace('. ', '.\n\n')
    text2 = text1.replace('? ', '?\n\n')
    final_text = text2.replace(': ', ':\n\n')

    for i in range(len(final_text)):
        if final_text[i] == ' ' and final_text[i + 1] == ' ':
            continue
        if (final_text[i] == ' ' and final_text[i - 1] == ' '
           and final_text[i + 1] != ' '):
            continue
        if final_text[i] == '.' and final_text[i + 1] != '\n':
            print(final_text[i], end="")
            print("\n")
            continue
        print(final_text[i], end="")
