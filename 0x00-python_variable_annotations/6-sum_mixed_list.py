#!/usr/bin/env python3
"""
Module demostrates typing in Python
"""


def sum_mixed_list(mxd_lst: list[int | float]) -> float:
    """
    typed function
    """
    sum_: float = 0.0

    for i in range(len(mxd_lst)):
        sum += mxd_lst[i]

    return sum_
