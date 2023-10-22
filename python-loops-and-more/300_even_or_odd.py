#!/usr/bin/python3

import random
random_num = random.randint(-10000, 10000)

num_str = repr(random_num)
last_digit_str = num_str[-1]
last_digit = int(last_digit_str)
if int(last_digit) == 0:
    print(f"{random_num} - the last digit {last_digit} is zero")
elif int(last_digit % 2) > 0:
    print(f"{random_num} - the last digit {last_digit} is odd")
else:
    print(f"{random_num} - the last digit {last_digit} is even")
