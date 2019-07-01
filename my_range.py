# coding: utf-8
"""My implementation of the range function in Python built-ins"""
from typing import *


def my_range(*args) -> Iterator[int]:
    start = 0
    step = 1
    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start, stop, step = args
    elif len(args) == 0:
        raise TypeError("range expected 1 arguments, got 0")
    else:
        raise TypeError("range expected at most 3 arguments, got {}".format(len(args)))

    if step == 0:
        raise ValueError("range() arg 3 must not be zero")

    if (stop - start) * step <= 0:
        return

    index = start
    if start <= stop:
        while index < stop:
            yield index
            index += step
    else:
        while index > stop:
            yield index
            index += step


def test_one_argument():
    assert list(my_range(0)) == list(range(0))
    assert list(my_range(5)) == list(range(5))


def test_two_arguments():
    assert list(my_range(0, 1)) == list(range(0, 1))
    assert list(my_range(0, 0)) == list(range(0, 0))
    assert list(my_range(10, 0)) == list(range(10, 0))
    assert list(my_range(1, 5)) == list(range(1, 5))
    assert list(my_range(-3, 10)) == list(range(-3, 10))
    assert list(my_range(-10, -3)) == list(range(-10, -3))


def test_three_arguments():
    assert list(my_range(1, 5, 10)) == list(range(1, 5, 10))
    assert list(my_range(10, 0, -1)) == list(range(10, 0, -1))
    assert list(my_range(10, 0, -20)) == list(range(10, 0, -20))
    assert list(my_range(10, 0, -2)) == list(range(10, 0, -2))
    assert list(my_range(0, 0, 1)) == list(range(0, 0, 1))
    assert list(my_range(0, 0, -1)) == list(range(0, 0, -1))


def test():
    test_one_argument()
    test_two_arguments()
    test_three_arguments()


if __name__ == "__main__":
    test()
