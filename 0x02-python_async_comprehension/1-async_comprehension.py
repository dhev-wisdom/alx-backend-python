#!/usr/bin/env python3
"""
Module demostrate async comprehension in Python
"""

import asyncio
async_generator = __import__('0-async_generator').async_generator
from typing import List


async def async_comprehension() -> List[float]:
    """
    async function
    """

    random_numbers = [i async for i in async_generator()]
    return random_numbers
