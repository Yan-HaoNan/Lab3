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