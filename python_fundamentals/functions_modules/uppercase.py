#!/usr/bin/env python3
def uppercase(str):
    result = ""

    for chars in str:
        if 97 <= ord(chars) <= 122:
            chars = chr(ord(chars) - 32)
        result += chars

    print("{}".format(result))
