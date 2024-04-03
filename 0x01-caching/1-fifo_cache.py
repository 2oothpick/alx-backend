#!/usr/bin/env python3
"""
module contains FIFO caching system
"""

# import BaseCaching from base_caching.py
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Class inherits BaseCaching and overrides
    its put and get methods
    """

    def __init__(self):
        """
        Initializes the class
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """
        Populates the self.cache_data dictionary
        if key and item are not None.
        Deletes the first item in the dictionary if
        the number of items exceed BaseCaching.MAX_ITEMS
        """
        if key is not None or item is not None:
            self.cache_data.update({key: item})
        if len(self.cache_data) > self.MAX_ITEMS:
            first_item = next(iter(self.cache_data))
            print(f"DISCARD: {first_item}")
            del self.cache_data[first_item]

    def get(self, key):
        """
        Returns dictionary values for the provided key
        if key exists in self.cache_data and key is
        not None, otherwise return None
        """
        return self.cache_data.get(key, None)
