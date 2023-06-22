import math
"""
Analysis of LBYL and EAFP styles

"""


def divide(x,y):
    if y == 0:
        return math.inf
    else:
        try:
            result = x / y
        except ZeroDivisionError:
            return math.inf
        return result