import pytest
import price_info


def test_total_cost_shopping():
    assert price_info.total_cost_shopping() == pytest.approx(46.75)


@pytest.mark.parametrize("fruit, quantity, expected", [("apple", 10, 12), ("orange", 5, 7), ("watermelon", 1, 6.5), ("pineapple", 2, 5.4), ("pear", 10, 9), ("papaya", 1, 2.95), ("pomegranate", 2, 9.9), ("apple", 0, 0)])
def test_cost_of_fruits(fruit, quantity, expected):
    assert price_info.cost_of_fruits(fruit, quantity) == pytest.approx(expected)


def test_total_cost_uses_matching_quantities(monkeypatch):
    monkeypatch.setattr(price_info, "price_list", {"apple": 2, "pear": 3})
    monkeypatch.setattr(price_info, "quantity_list", {"apple": 4, "unknown": 99})
    assert price_info.total_cost_shopping() == 8


def test_empty_shopping(monkeypatch):
    monkeypatch.setattr(price_info, "quantity_list", {})
    assert price_info.total_cost_shopping() == 0
