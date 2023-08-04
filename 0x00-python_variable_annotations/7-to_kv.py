#!/usr/bin/env python3
"""
Module demostrate Python as a typed language
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    advanced typed function
    """
    return k, v ** 2.0
