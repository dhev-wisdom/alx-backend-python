#!/usr/bin/env python3
"""
Module demotrates typing in Python
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    funtion returns function
    """
    def func(f: float) -> float:
        """
        inner function
        """
        return multiplier * f

    return func
