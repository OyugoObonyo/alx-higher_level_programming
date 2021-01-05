#!/usr/bin/python3
"""Define a class called square"""


class Square:
    """class with size as private instance attribute"""
    def __init__(self, size=0):
        """initialize the class"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
