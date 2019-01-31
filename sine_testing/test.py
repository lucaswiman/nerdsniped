import math
from functools import partial

import pytest
from hypothesis import strategies as st
from hypothesis import given
from scipy.misc import derivative

import trig


π = math.pi


def test_sine_of_zero_is_zero():
    assert trig.sin(0) == 0

def test_known_values():
    assert trig.sin(π) == pytest.approx(0)
    assert trig.sin(π / 2) == pytest.approx(1)
    assert trig.sin(π / 4) == pytest.approx(math.sqrt(1 / 2))
    assert trig.sin(2 * π / 3) == pytest.approx(math.sqrt(3) / 2)


@given(st.integers(min_value=-100, max_value=100),
       st.floats(min_value=-π, max_value=π))
def test_periodicity(period, value):
    assert trig.sin(value) == pytest.approx(trig.sin(value + period * 2 * π))


@given(st.floats(min_value=-π, max_value=π))
def test_negative_function(value):
    assert trig.sin(-value) == pytest.approx(-trig.sin(value))


def numerical_derivative(f, tol=1e-6):
    def f_prime(x):
        return derivative(f, x, dx=tol)

    return f_prime


@given(st.floats(min_value=-π, max_value=π)
       .filter(lambda x: abs(x) > 1e-2))
def test_differential_equations(value):
    # Verifies that sin satisfies f''=-f and f'=cos
    first_derivative = numerical_derivative(trig.sin)
    second_derivative = numerical_derivative(first_derivative)
    assert abs(first_derivative(value) - trig.cos(value)) == pytest.approx(0)
    assert abs(second_derivative(value) - -second_derivative(value)) == pytest.approx(0, abs=1e-4)
