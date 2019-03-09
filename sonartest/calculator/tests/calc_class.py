"""
calc_class.py contains the Calculator class.
It uses the math functions from calc_func.
"""

# from .calc_func import *
"""
calc_func.py contains math functions with no side effects.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # automatically raises ZeroDivisionError
    return a * 1.0 / b


def maximum(a, b):
    return a if a >= b else b


def minimum(a, b):
    return a if a <= b else b


class Calculator(object):
    def __init__(self):
        self._last_answer = 0.0

    @property
    def last_answer(self):
        return self._last_answer

    def _do_math(self, a, b, func):
        self._last_answer = func(a, b)
        return self.last_answer

    def add(self, a, b):
        return self._do_math(a, b, add)

    def subtract(self, a, b):
        return self._do_math(a, b, subtract)

    def multiply(self, a, b):
        return self._do_math(a, b, multiply)

    def divide(self, a, b):
        return self._do_math(a, b, divide)

    def maximum(self, a, b):
        return self._do_math(a, b, maximum)

    def minimum(self, a, b):
        return self._do_math(a, b, minimum)
