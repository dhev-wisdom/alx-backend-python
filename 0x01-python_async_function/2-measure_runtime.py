#!/usr/bin/env python3
"""
Module demostrates Asynchronous programming in Python
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    async function
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total = end - start
    average = total / n
    return average
