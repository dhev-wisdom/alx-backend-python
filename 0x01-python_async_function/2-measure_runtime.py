#!/usr/bin/env python3
"""
Module demostrates Asynchronous programming in Python
"""

import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    async function
    """
    start_time = time.perf_counter()
    wait_n(n, max_delay)
    total_time = time.perf_counter() - start_time
    return total_time / n
