#!/usr/bin/python3

list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5
old_list_ = list_


def replace_element(list_, index):
    if index < 0 or index > len(list_) - 1:
        print(list_)
        return None
    else:
        old_list_ = list_[:]
        list_[index] = element_to_replace
        print(f"Copy:     {list_}")
        print(f"Original: {old_list_}")
        return list_[index]


replace_element(list_, index)
