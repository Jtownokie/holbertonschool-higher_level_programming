#!/usr/bin/python3
""" This Module contains a function that adds newlines in a string """


def text_indentation(text):
    """ This Function adds two newlines after every ., ?, and : """
    if type(text) is not str:
        raise TypeError('text must be a string')

    text1 = text.replace('. ', '.\n\n')
    text2 = text1.replace('.', '.\n\n')
    text3 = text2.replace('? ', '?\n\n')
    final_text = text3.replace(': ', ':\n\n')

    print(final_text, end="")
