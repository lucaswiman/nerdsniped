import math

import pytest

import trig


π = math.pi


def test_sine_of_zero_is_zero():
    assert trig.sin(0) == 0

def test_known_values():
    assert trig.sin(π) == pytest.approx(0)
    assert trig.sin(π / 2) == pytest.approx(1)
    assert trig.sin(π / 4) == pytest.approx(math.sqrt(1 / 2))
    assert trig.sin(2 * π / 3) == pytest.approx(math.sqrt(3) / 2)
