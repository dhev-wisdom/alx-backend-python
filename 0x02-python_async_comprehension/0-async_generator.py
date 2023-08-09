#!/usr/bin/emv python3
"""
Python Async Comprehension
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    async function
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
