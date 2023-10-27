#!/usr/bin/python3

if __name__ == "__main__":
    import calculation

    a = 4  # use this variable as a first argument to call a function
    b = 2  # use this variable as a second argument to call a function

#  ADD YOUR CODE HERE
print(f"{a} + {b} = {calculation.add(a, b)}")
print(f"{a} - {b} = {calculation.sub(a, b)}")
print(f"{a} * {b} = {calculation.mul(a, b)}")
print(f"{a} / {b} = {calculation.div(a, b)}")
