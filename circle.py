import math


def area(r):
    if type(r) == str:
        return "arguments must be integer"
    if r < 0:
        return "arguments must be positive"
    return math.pi * r * r


def perimeter(r):
    if type(r) == str:
        return "arguments must be integer"
    if r < 0:
        return "arguments must be positive"
    return 2 * math.pi * r
