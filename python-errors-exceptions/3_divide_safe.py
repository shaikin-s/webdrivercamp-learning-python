#!/usr/bin/python3

def divide_safe(a, b):
    result = 0
    try:
        result = a / b
    except (ZeroDivisionError, ValueError, TypeError):
        result = None
    finally:
        print(f"Result: {result}")
    return result


if __name__ == "__main__":
    a = 9
    b = 3
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")

    b = 0
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")
