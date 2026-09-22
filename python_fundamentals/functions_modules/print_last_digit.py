#!/usr/bin/env python3
def print_last_digit(number):
    if number > 0:
        digit = abs(number) % 10
    if number < 0:
        digit = (abs(number) % 10)
    if number == 0:
        digit = 0
    print("{}".format(digit), end="")
    return (digit)
