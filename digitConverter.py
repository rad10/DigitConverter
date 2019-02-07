#!/bin/python
# from math import pow

# Binary


""" def fromBinary(binary):
    Binary = []
    for i in range(0, len(str(binary))):
        Binary.append(int(str(binary)[i]))
    Binary.reverse()
    dec = 0
    for i in range(0, len(str(binary))):
        dec = dec + (int(Binary[i]) * pow(2, i))
    return int(dec) """


def fromBinary(binary: int) -> int:
    """ From binary takes an int binary strand and converts it into a decimal number that represents the strand """
    bin = int(binary) # this was needed incase they gave something else like a string or a double
    dec = exp = 0
    while (bin > 0):  # this would whittle down the number until it got to 0
        # This line made it so that every addition added to its total. bin % 10 gave me the digit at the very end. I used to use pow, but ** gave the same result without importing a library
        dec = dec + int((bin % 10) * 2 ** exp)
        bin //= 10 # doing this permanent change allowed me to get each digit in the line in reverse
        exp += 1
    return dec


""" def toBinary(dec):
    dec = int(dec)
    Binary = []
    while (dec > 0):
        Binary.append(str(dec % 2))
        dec = ((dec - (dec % 2)) / 2)
    Binary.reverse()
    binary = ""
    for i in range(0, len(Binary)):
        binary = (str(binary) + str(Binary[i]))
    return int(binary) """

def toBinary(dec: int) -> int:
    """ To Binary take a decimal number and converts it into an int Binary strand """
    dec = int(dec)
    binary = ""  # To make the strand, I used a string so that each digit would sit side by side without adding together
    # I could have done it without a string, but it would have required and extra exponent int to keep track of position.
    while (dec > 0):
        binary = str(dec % 2) + binary # i could have done it with an if statement between 0/1, but this was easier and worked better for the other formats
        dec //= 2 # the //= means an even division, dropping the remainder. a decimal number would have destroyed it.
    return int(binary) # in the end convert the string into a number for returning
# /Binary
# Octal


""" def fromOctal(octal):
    Octal = []
    for i in range(0, len(str(octal))):
        Octal.append(int(str(octal)[i]))
    Octal.reverse()
    dec = 0
    for i in range(0, len(str(octal))):
        dec = dec + (int(Octal[i]) * pow(8, i))
    return int(dec) """


def fromOctal(octal: int) -> int:
    """ From Octal takes a strand in octal and converts it into a decimal number """
    oct = int(octal)
    dec = exp = 0
    while (oct > 0):
        dec = dec+int((oct % 10) * 8 ** exp)
        # print("oct:", oct)
        # print("dec:",dec)
        oct //= 10
        exp += 1
        # print("exp:",exp)
    return int(dec)


""" def toOctal(dec):
    dec = int(dec)
    Octal = []
    while (dec > 0):
        Octal.append(str(dec % 8))
        dec = ((dec - (dec % 8)) / 8)
    Octal.reverse()
    octal = ""
    for i in range(0, len(Octal)):
        octal = (str(octal) + str(Octal[i]))
    return int(octal) """


def toOctal(dec: int) -> int:
    """ To Octal takes a decimal number and converts it into an octal strand """
    dec = int(dec)
    octal = ""
    while (dec > 0):
        octal = str(dec % 8) + octal
        dec //= 8
    return int(octal)
# /Octal
# Decimal

# /Decimal
# Hexadecimal

# /Hexadecimal
