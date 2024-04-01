#!/usr/bin/env python3
"""
0-simple_helper_function
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple with start and end indexes
    """
    return ((page - 1) * page_size, (page * page_size))
