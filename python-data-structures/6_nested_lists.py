#!/usr/bin/python3

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print(val, end=" ")
        print()


print_matrix(matrix)
