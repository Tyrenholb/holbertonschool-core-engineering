#!/usr/bin/env python3
"""Define a square class."""

class Square:
    """This is my square class"""

    def __init__(self, size):
        """Set the square's size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("Size must bne >= 0")
        self.__size = size
