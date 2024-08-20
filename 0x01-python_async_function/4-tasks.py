#!/usr/bin/env python3
""" Aynchronous Function """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


asyn def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous function
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]