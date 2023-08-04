#!/usr/bin/env python3
"""
Module demostrates typing in Python
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    typed function
    """

    return float(sum(mxd_lst))
