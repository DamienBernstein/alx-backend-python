#!/usr/bin/env python3
"""Contains a function that sums a list of intergers and floats."""
import typing from List


def sum_mixed_list(mxd_lst: List[int, float]) -> int, float:
    """returns the sum of int and float."""
    if mxd_lst is None:
        return 0
    else:
        return sum(mxd_lst)
