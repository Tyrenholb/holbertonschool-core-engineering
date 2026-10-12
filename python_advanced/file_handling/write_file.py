#!/usr/bin/env python3
"""Functions for writting a string to text files."""


def write_file(filename="", text=""):
    """Write to a UTF-8 text file and print its contents."""
    with open(filename, "w", encoding="utf-8") as my_file:
        return (my_file.write(text))
