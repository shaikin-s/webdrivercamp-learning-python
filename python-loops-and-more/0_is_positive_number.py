#!/usr/bin/python3

import random

random_num = random.randint(-10, 10)
a: str = "is zero"
b: str = "is negative"
c: str = "is positive"
if random_num == 0:
    print(f"{random_num} {a}")
elif random_num > 0:
    print(f"{random_num} {c}")
else:
    print(f"{random_num} {b}")
