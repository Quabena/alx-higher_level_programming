#!/usr/bin/python3

def no_c(my_string):
    res_string = ""

    for char in my_string:
        if char != 'c' and char != 'C':
            res_string += char

    return res_string
