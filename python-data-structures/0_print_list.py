#!/usr/bin/python3

list_ = [5, 4, 3, 2, 1]


def print_int(list_):
    for i in range(len(list_)):
        if isinstance(list_[i], int):
            print(f"{list_[i]}")


print_int(list_)
