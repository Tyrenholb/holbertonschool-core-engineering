#!/usr/bin/env python3
"""Define a square class."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a validated size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Return the square's position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the square's position after validation."""
        if (
            type(value) is not tuple
            or len(value) != 2
            or any(type(item) is not int or item < 0 for item in value)
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        self.__position = value

    def __str__(self):
        """Return the square as a string with its position offset."""
        if self.__size == 0:
            return ""

        x, y = self.__position
        row = " " * x + "#" * self.__size
        return "\n" * y + "\n".join(row for _ in range(self.__size))

    def my_print(self):
        """Print the square with the character #."""
        print(self)
