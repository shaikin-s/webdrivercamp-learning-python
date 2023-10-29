#!/usr/bin/python3

list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5


def replace_element(list_, index):
    if index < 0 or index > len(list_) - 1:
        print(list_)
        return None
    else:
        list_[index] = element_to_replace
        print(f"{list_}")
        return list_[index]


replace_element(list_, index)
