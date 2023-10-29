#!/usr/bin/python3

def tuple_addition(first_arg=(), second_arg=()):
    first_element = first_arg[0] if len(first_arg) >= 1 else 0
    second_element = first_arg[1] if len(first_arg) >= 2 else 0
    third_element = second_arg[0] if len(second_arg) >= 1 else 0
    fourth_element = second_arg[1] if len(second_arg) >= 2 else 0

    result = (first_element + third_element, second_element + fourth_element)

    return result
