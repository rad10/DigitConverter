#!/bin/python
from math import pow

# Binary


def fromBinary(binary):
    Binary = []
    for i in range(0, len(str(binary))):
        Binary.append(int(str(binary)[i]))
    Binary.reverse()
    dec = 0
    for i in range(0, len(str(binary))):
        dec = dec + (int(Binary[i]) * pow(2, i))
    return int(dec)


def fromBinaryv2(binary):
    bin = int(binary)
    dec = exp = 0
    while (bin > 0):
        dec = dec + int((bin % 10) * 2 ** exp)
        bin //= 10
        exp += 1
    return dec


def toBinary(dec):
    dec = int(dec)
    Binary = []
    while (dec > 0):
        Binary.append(str(dec % 2))
        dec = ((dec - (dec % 2)) / 2)
    Binary.reverse()
    binary = ""
    for i in range(0, len(Binary)):
        binary = (str(binary) + str(Binary[i]))
    return int(binary)


def toBinaryv2(dec):
    dec = int(dec)
    binary = ""
    while (dec > 0):
        binary = str(dec % 2) + binary
        dec //= 2
    return int(binary)
# /Binary
# Octal


def fromOctal(octal):
    Octal = []
    for i in range(0, len(str(octal))):
        Octal.append(int(str(octal)[i]))
    Octal.reverse()
    dec = 0
    for i in range(0, len(str(octal))):
        dec = dec + (int(Octal[i]) * pow(8, i))
    return int(dec)


def fromOctalv2(octal):
    oct = int(octal)
    dec = exp = 0
    while (oct > 0):
        dec = dec+int((oct % 10) * 8 ** exp)
        #print("oct:", oct)
        # print("dec:",dec)
        oct //= 10
        exp += 1
        # print("exp:",exp)
    return int(dec)


def toOctal(dec):
    dec = int(dec)
    Octal = []
    while (dec > 0):
        Octal.append(str(dec % 8))
        dec = ((dec - (dec % 8)) / 8)
    Octal.reverse()
    octal = ""
    for i in range(0, len(Octal)):
        octal = (str(octal) + str(Octal[i]))
    return int(octal)


def toOctalv2(dec):
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


def test():
    print(toOctal(15))
    print(toOctalv2(15))


test()
