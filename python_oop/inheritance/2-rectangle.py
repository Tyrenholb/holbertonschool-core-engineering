#!/usr/bin/env python3
"""Define a rectangle with area and string representation."""


BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle with private width and height."""

    def __init__(self, width, height):
        """Validate and store the rectangle dimensions."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the rectangle's area."""
        return self.__width * self.__height

    def __str__(self):
        """Return a readable description of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
