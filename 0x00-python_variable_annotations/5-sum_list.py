#!/usr/bin/env python3
"""
Module demostrates typing in Python
"""


def sum_list(input_list: list[float]) -> float:
    """
    typed function
    """
    sum: float = 0.0

    for i in input_list:
        sum += i

    return sum
