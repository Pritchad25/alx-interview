#!/usr/bin/python3
"""Module for UTF-8 Validation """


def validUTF8(data):
    """
    This method determines if a given data set represents a valid UTF-8
    encoding.
    Returns: True if data is a valid UTF-8 encoding, else return False
    """

    nbytes = 0

    for byte in data:
        if nbytes == 0:
            if (byte >> 7) == 0b0:
                continue
            elif (byte >> 5) == 0b110:
                nbytes = 1
            elif (byte >> 4) == 0b1110:
                nbytes = 2
            elif (byte >> 2) == 0b11110:
                nbytes = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            nbytes -= 1
    return nbytes == 0
