from math import pi, sqrt, pow, hypot


def test_filter():
    nums = filter(lambda i: i % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert list(nums) == [2, 4, 6, 8]


def test_map():
    nums = map(lambda i: i * i, [1, 2, 3, 4, 5, 6, 7, 8])
    assert list(nums) == [1, 4, 9, 16, 25, 36, 49, 64]


def test_sorted():
    assert sorted([2, 1, 5, 4, 3]) == [1, 2, 3, 4, 5]


def test_math_pi():
    assert round(pi, 2) == 3.14


def test_math_sqrt():
    assert sqrt(64) == 8


def test_math_pow():
    assert pow(3, 2) == 9


def test_math_hypot():
    assert round(hypot(3, 2), 2) == 3.61
