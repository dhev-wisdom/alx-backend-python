#!/usr/bin/env python3
"""
Module demostrate Python as a typed language
"""

def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """
    advanced typed function
    """
    t : tuple[str, float] = (k, float(v**2))
    return t
