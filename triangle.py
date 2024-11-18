import math


def area(a, b, c):
    if isinstance(a, str) or isinstance(b, str) or isinstance(c, str):
        return "arguments must be integer"
    if a < 0 or b < 0 or c < 0:
        return "arguments must be positive"
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def perimeter(a, b, c):
    if isinstance(a, str) or isinstance(b, str) or isinstance(c, str):
        return "arguments must be integer"
    if a < 0 or b < 0 or c < 0:
        return "arguments must be positive"
    return a + b + c
