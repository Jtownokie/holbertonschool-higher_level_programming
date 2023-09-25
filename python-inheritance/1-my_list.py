#!/usr/bin/python3
""" This Module contains the MyList Class """


class MyList(list):
    """ This Class is derived from the 'list' type and can sort a list """
    def print_sorted(self):
        """ This method prints a sorted list """
        print(sorted(self))
