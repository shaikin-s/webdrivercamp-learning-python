#!/usr/bin/python3

list_ = [5, 4, 3, 2, 1]
index = 2


def retrieve_and_print(list_, index):
    if index < 0 or index > len(list_) - 1:
        return None
    else:
        print(f"The element retrieved is {list_[index]}")
        return list_[index]


retrieve_and_print(list_, index)
