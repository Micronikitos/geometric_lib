def area(a):
    if isinstance(a) == str:
        return "arguments must be integer"
    if a < 0:
        return "arguments must be positive"
    return a * a


def perimeter(a):
    if isinstance(a) == str:
        return "arguments must be integer"
    if a < 0:
        return "arguments must be positive"
    return 4 * a
