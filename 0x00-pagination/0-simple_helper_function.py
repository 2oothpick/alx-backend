#!/usr/bin/env python3
"""
0-simple_helper_function.py
"""

def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Returns a tuple with start and end indexes
    """
    return ((page -1) * page_size , (page * page_size))