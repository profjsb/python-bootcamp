from pocket.ops import addition, subtraction, division


def test_addition_zero():
    assert addition(3, 0) == 3


def test_addition():
    assert addition(0, 1) == 1


def test_subtraction():
    assert subtraction(1, 4) == -3


def test_division():
    assert division(10, 2) == 5


def test_division_float():
    assert division(5, 2) == 2.5
