#!/usr/bin/env python3
"""Define a square class."""

# public class self.size for public use.
class Square:
    """Blah blah blah"""
# private class
    def __init__(self, size):
        """Set the square's size."""
        self.__size = size #internal use only

# self.__size private instance attribute through pythons name mangling.
