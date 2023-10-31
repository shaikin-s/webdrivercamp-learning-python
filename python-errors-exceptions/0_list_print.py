#!/usr/bin/python3

def list_print(lst=[], i=0):
    count = 0
    for value in lst[:i]:
        try:
            print(f"{(value)}", end="")
            count += 1
        except IndexError:
            print()
    print()
    return count


if __name__ == "__main__":
    list_ = [1, 2, 3, 4, 5, 6, 7]

    count = list_print(list_, 4)
    print(f"Count: {count:d}")
    count = list_print(list_, len(list_))
    print(f"Count: {count:d}")
    count = list_print(list_, len(list_) + 2)
    print(f"Count: {count:d}")
