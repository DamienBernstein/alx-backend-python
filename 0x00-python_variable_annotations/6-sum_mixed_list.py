#!/usr/bin/env python3
"""Contains a function that sums a list of intergers and floats."""
import typing from List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum of int and float."""
     return sum(mxd_lst)
