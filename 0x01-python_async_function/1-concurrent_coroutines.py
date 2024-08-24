#!/usr/bin/env  python3
""" Aynchronous Function
"""

import asyncio
from typing import List
import heapq

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times with the specified max_delay
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        heapq.heappush(delays, delay)

    return [heapq.heappop(delays) for _ in range(len(delays))]
