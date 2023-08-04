#!/usr/bin/env python3
"""
Module demotrates typing in Python
"""
from typing import Iterable, Tuple, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    funtion returns function
    """
    return [(i, len(i)) for i in lst]
