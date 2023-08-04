#!/usr/bin/env python3
"""
Module demotrates typing in Python
"""
from typing import Iterable, Sequence, Any, Union


def safe_first_element(lst: Iterable[Sequence]) -> Union[Any,  None]:
    if lst:
        return lst[0]
    else:
        return None
