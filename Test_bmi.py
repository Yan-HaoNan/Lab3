from Lab2 import bmi

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(height=1.70, weight=65)
    assert result == 0

def test_bmi_over_weight():
    result = bmi.calculate_bmi(height=1.70, weight=80)
    assert result == 1

def test_bmi_under_weight():
    result = bmi.calculate_bmi(height=1.70, weight=45)
    assert result == -1

import pytest


@pytest.mark.parametrize("weight, expected", [(18.49, -1), (18.5, 0), (25.0, 0), (25.01, 1)])
def test_bmi_boundaries(weight, expected):
    # Height 1 makes weight numerically equal to BMI for exact boundaries.
    assert bmi.calculate_bmi(height=1, weight=weight) == expected
