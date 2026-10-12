#!/usr/bin/env python3
"""text"""


def append_write(filename="", text=""):
    """Append to utf-8 textfile and print its content"""
    with open(filename, "a", encoding="utf-8") as my_file:
        return (my_file.write(text))
