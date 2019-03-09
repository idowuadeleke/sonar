"""
test_calc_class.py contains pytest tests for the Calculator class.
pytest discovers tests named "test_*".
pytest can run test classes, but functions are a better way.
Each test function uses a fixture for setup.
Compare this example to test_calc.py in example-py-unittest.
"""

import pytest
#from .calc_class import Calculator
#from sonartest.calculator.function_example.calc_class import *

# "Constants"
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


NUMBER_1 = 3.0
NUMBER_2 = 2.0


# Fixtures

@pytest.fixture
def calculator():
    return Calculator()


# Helpers

def verify_answer(expected, answer, last_answer):
    assert expected == answer
    assert expected == last_answer


# Test Cases

def test_last_answer_init(calculator):
    assert calculator.last_answer == 0.0


def test_add(calculator):
    answer = calculator.add(NUMBER_1, NUMBER_2)
    verify_answer(5.0, answer, calculator.last_answer)


def test_subtract(calculator):
    answer = calculator.subtract(NUMBER_1, NUMBER_2)
    verify_answer(1.0, answer, calculator.last_answer)


def test_subtract_negative(calculator):
    answer = calculator.subtract(NUMBER_2, NUMBER_1)
    verify_answer(-1.0, answer, calculator.last_answer)


def test_multiply(calculator):
    answer = calculator.multiply(NUMBER_1, NUMBER_2)
    verify_answer(6.0, answer, calculator.last_answer)


def test_divide(calculator):
    answer = calculator.divide(NUMBER_1, NUMBER_2)
    verify_answer(1.5, answer, calculator.last_answer)


# Test for dividing by zero catches the exception
# http://doc.pytest.org/en/latest/assert.html#assertions-about-expected-exceptions

def test_divide_by_zero(calculator):
    with pytest.raises(ZeroDivisionError) as e:
        calculator.divide(NUMBER_1, 0)
    assert "division by zero" in str(e.value)


# Tests for maximum and minimum use parameters
# To use the fixture, put it as the first function argument
# http://doc.pytest.org/en/latest/parametrize.html

@pytest.mark.parametrize("a,b,expected", [
    (NUMBER_1, NUMBER_2, NUMBER_1),
    (NUMBER_2, NUMBER_1, NUMBER_1),
    (NUMBER_1, NUMBER_1, NUMBER_1),
])
def test_maximum(calculator, a, b, expected):
    answer = calculator.maximum(a, b)
    verify_answer(expected, answer, calculator.last_answer)


@pytest.mark.parametrize("a,b,expected", [
    (NUMBER_1, NUMBER_2, NUMBER_2),
    (NUMBER_2, NUMBER_1, NUMBER_2),
    (NUMBER_2, NUMBER_2, NUMBER_2),
])
def test_minimum(calculator, a, b, expected):
    answer = calculator.minimum(a, b)
    verify_answer(expected, answer, calculator.last_answer)
