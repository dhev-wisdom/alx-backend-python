#!/usr/bin/env python3
"""
Module demostrates Asynchronous programming in Python
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    async function
    """
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return (i)
