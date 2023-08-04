#!/usr/bin/env python3
"""
Module demotrates typing in Python
"""
from typing import Any, Union, Optional, TypeVar, Mapping


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any, default: Optional[T] = None) -> Union[Any, T]:
    """
    typex python function
    """
    if key in dct:
        return dct[key]
    else:
        return default
