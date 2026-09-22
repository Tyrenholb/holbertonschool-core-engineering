#!/usr/bin/env python3
def print_last_digit(number):
    if number > 0:
        digit = abs(number) % 10
    else:
        number < 0
        digit = -(abs(number) % 10)
    print("{}".format(digit))
