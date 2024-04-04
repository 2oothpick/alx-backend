#!/usr/bin/env python3

"""
module contains LIFO caching system
"""
from collections import OrderedDict

# import BaseCaching from base_caching.py

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Class inherits BaseCaching and overrides
    its put and get methods to implement caching
    systems
    """

    def __init__(self):
        """
        Initializes the class
        """
        super().__init__()
        self.cache_data = OrderedDict()
        # OrderedDict: dict subclassthat remembers the order
        # entries were added

    def put(self, key, item):
        """
        Populates the self.cache_data dictionary
        if key and item are not None.
        Deletes the last added item in the dictionary if
        the number of items exceeds BaseCaching.MAX_ITEMS
        """
        if key is None or item is None:
            return
        if key is not None or item is not None:
            if key not in self.cache_data:
                # if item is a new item, check if dictionary is full
                # before adding
                if len(self.cache_data) >= self.MAX_ITEMS:
                    # if dictionay is full, remove last item
                    last_item, val = self.cache_data.popitem(last=True)
                    print(f"DISCARD: {last_item}")
            self.cache_data.update({key: item})
            # move most recently added item to the end
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        Returns dictionary values for the provided key
        if key exists in self.cache_data and key is
        not None, otherwise return None
        """
        return self.cache_data.get(key, None)
