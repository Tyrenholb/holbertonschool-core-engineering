#!/usr/bin/env python3
"""Define a square class."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize the square with a validated size."""
        self.size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    @property
    def size(self):
        """Return the square's size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the square's size after validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints in stdout the square with the character"""
        if self.size == 0:
            print("")
        else:
            for _ in range(self.size):
                print("#" * self.size)
