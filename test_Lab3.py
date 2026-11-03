import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

# Table 3: REQ-03, REQ-04 and REQ-05.
import pytest


@pytest.mark.parametrize("count", [10, 11, 20])
def test_bubble_sort_too_many_numbers(count):
    assert Lab3.bubble_sort(list(range(count)), Lab3.SORT_ASCENDING) == 1


def test_bubble_sort_empty():
    assert Lab3.bubble_sort([], Lab3.SORT_ASCENDING) == 0


@pytest.mark.parametrize("value", [1.5, "2", None, True])
def test_bubble_sort_non_integer(value):
    assert Lab3.bubble_sort([1, value, 3], Lab3.SORT_ASCENDING) == 2


@pytest.mark.parametrize("order, expected", [(Lab3.SORT_ASCENDING, [-3, -1, 0, 2, 2, 4, 5, 6, 9]), (Lab3.SORT_DESCENDING, [9, 6, 5, 4, 2, 2, 0, -1, -3])])
def test_bubble_sort_nine_numbers(order, expected):
    values = [2, -1, 9, 0, 2, 6, -3, 4, 5]
    original = values.copy()
    assert Lab3.bubble_sort(values, order) == expected
    assert values == original


@pytest.mark.parametrize("order", [Lab3.SORT_ASCENDING, Lab3.SORT_DESCENDING])
def test_bubble_sort_single_number(order):
    assert Lab3.bubble_sort([7], order) == [7]


def test_bubble_sort_invalid_order_single_number():
    assert Lab3.bubble_sort([7], 3) == []
