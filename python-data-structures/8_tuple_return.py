#!/usr/bin/python3

def tuple_return(arg):
    list_len = len(arg)
    first_element = arg[0]
    if list_len > 0:
        return list_len, first_element
    else:
        None
