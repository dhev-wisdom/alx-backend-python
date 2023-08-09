#!/usr/bin/env python3
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension

"""
Module for Asynchronous Python Programming
"""


async def measure_runtime() -> float:
    """
    async fuction using asyncio.gather()
    """
    funcs = [async_comprehension() for _ in range(4)]
    start_time = time.perf_counter()
    await asyncio.gather(*funcs)
    total_time = time.perf_counter() - start_time
    return total_time
