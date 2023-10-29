#!/usr/bin/python3

string = """AbraCadabra
A new string voila!"""


def remove_char(some_string):
    a = ""
    for i in some_string:
        if i == 'a' or i == 'A':
            a += ""
        else:
            a += i
    print(a)


remove_char(string)
