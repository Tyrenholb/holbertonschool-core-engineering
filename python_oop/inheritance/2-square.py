#!/usr/bin/env python3
"""Define a square with its own string representation."""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square with a private size."""

    def __init__(self, size):
        """Validate size and initialize equal dimensions."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the square's area."""
        return self.__size * self.__size

    def __str__(self):
        """Return a readable description of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
