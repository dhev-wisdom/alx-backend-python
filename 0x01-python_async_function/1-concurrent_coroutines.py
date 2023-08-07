#!/usr/bin/env python3
"""
Module demostrates Asynchronous programming in Python
"""

import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    async function
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
