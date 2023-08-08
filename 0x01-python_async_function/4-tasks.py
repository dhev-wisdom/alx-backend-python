#!/usr/bin/env python3
"""
Module demostrates python async await
"""

import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int):
    """
    use asyncio.Task to replicate an async function
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
