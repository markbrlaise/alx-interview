#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data: list):
    """
    function to check if data is a valid UTF-8
    encoding
    data: list of integers
    Return: True if data is a valid UTF-8
    encoding, else return False
    """
    byte_counter = 0

    for i in data:
        if byte_counter == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                byte_counter = 1
            elif i >> 4 == 0b1110:
                byte_counter = 2
            elif i >> 3 == 0b11110:
                byte_counter = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            byte_counter -= 1
    return byte_counter == 0