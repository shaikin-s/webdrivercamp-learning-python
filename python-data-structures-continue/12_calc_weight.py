#!/usr/bin/python3

def calc_weight(list_=[]):
    if not list_:
        return 0
    else:
        average = 0
        value = 0
        for i in list_:
            value += (i[0] * i[1])
            average += (i[1])
    return value / average


if __name__ == "__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 9 + 7)
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")
