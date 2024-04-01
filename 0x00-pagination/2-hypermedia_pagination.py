#!/usr/bin/env python3
"""
2. Hypermedia pagination
"""

import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple with start and end indexes
    """
    return ((page - 1) * page_size, (page * page_size))


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        corrects pagination
        """
        assert (isinstance(page, int) and isinstance(
            page_size, int) and page > 0 and page_size > 0)
        # unpack index_range tuple
        start, end = index_range(page, page_size)
        csv_length = len(self.dataset())
        # end index should be the min of end and size of dataset
        end = min(end, csv_length)
        # return empty list if input argument is out of range
        if start >= csv_length:
            return []
        return self.dataset()[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str: Any]:
        """
        Returns a dictionary with pagination information
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        if page + 1 <= total_pages:
            next_page = page + 1
        else:
            next_page = None
        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None
        return {'page_size': page_size,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
