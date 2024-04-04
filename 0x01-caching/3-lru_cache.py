#!/usr/bin/env python3

"""
module contains LRU caching system
"""
from collections import OrderedDict

# import BaseCaching from base_caching.py

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Class inherits BaseCaching and overrides
    its put and get methods
    """

    def __init__(self):
        """ Init
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Populates the self.cache_data dictionary
        if key and item are not None.
        Deletes the least used item in the dictionary if
        the number of items exceed BaseCaching.MAX_ITEMS
        """
        if key is not None or item is not None:
            if key not in self.cache_data:
                # if item is a new item, check if dictionary is full
                # before adding
                if len(self.cache_data) >= self.MAX_ITEMS:
                    # if dictionay is full, remove last item
                    least_used, val = self.cache_data.popitem()
                    print(f"DISCARD: {least_used}")
            self.cache_data.update({key: item})
            # move most recently used items to front
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """
        Returns dictionary values for the provided key
        if key exists in self.cache_data and key is
        not None, otherwise return None
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
