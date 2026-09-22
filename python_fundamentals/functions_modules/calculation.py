#!/usr/bin/env python3

if __name__ == "__main__":
    from calculator_1 import add
    from calculator_1 import subtract
    from calculator_1 import divide
    from calculator_1 import times
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, subtract(a, b)))
    print("{} / {} = {}".format(a, b, divide(a, b)))
    print("{} * {} = {}".format(a, b, times(a, b)))
