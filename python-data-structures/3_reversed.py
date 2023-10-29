#!/usr/bin/python3

list_ = [5, 4, 3, 2, 1]


def print_int(list_):
    n = len(list_)

    for i in range(n):
        for j in range(0, n - i - 1):
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]

    for element in list_:
        print(element)


print_int(list_)
