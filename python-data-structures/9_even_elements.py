#!/usr/bin/python3

my_list = [5, 4, 3, 2, 1]

tuple_even = tuple(i % 2 == 0 for i in my_list)

print(my_list)
print(tuple_even)
