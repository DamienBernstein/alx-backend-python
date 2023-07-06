#!/usr/bin/env python3
"""Contains function sum_list which takes a list of floats and returns their sum."""


def sum_list(input_list: list[float]) -> float:
    """Returns the sum of the input_list."""
    if input_list is None:
        return 0
    else:
        return sum(input_list)
