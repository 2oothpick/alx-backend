#!/usr/bin/python3
"""
100-lfu_cache
"""
# import BaseCaching from base_caching.py

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Class inherits BaseCaching and overrides
    its put and get methods.

    To implement LFU, a dictionary, self.uses, records
    the frequency with which items are accessed, items with
    least frequency is removed
    """

    def __init__(self):
        """
        Initializes the class
        """
        super().__init__()
        # dictionary record of the number of times
        # an item is accessed
        self.uses = dict()

    def put(self, key, item):
        """
        Populates the self.cache_data dictionary
        if key and item are not None.
        Deletes the least frequently used item in the dictionary if
        the number of items exceed BaseCaching.MAX_ITEMS
        """
        if (key is None or item is None):
            return
        # Before adding a new key, value pair (item) to the cache
        # check if it's full, if it is, remove least used item
        if (len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS
           and key not in self.cache_data.keys()):
            discard_key = min(self.uses, key=self.uses.get)
            del self.cache_data[discard_key]
            del self.uses[discard_key]
            print("DISCARD: {}".format(discard_key))
        # increment the key's value by 1 if it is
        # in self.cache_data
        if (key in self.cache_data.keys()):
            self.uses[key] += 1
        # else set its value to 1
        else:
            self.uses[key] = 1
        # update self.cache_data
        self.cache_data[key] = item

    def get(self, key):
        """
        Returns dictionary values for the provided key
        if key exists in self.cache_data and key is
        not None, otherwise return None
        """
        if (key is None or key not in self.cache_data.keys()):
            return
        self.uses[key] += 1
        return self.cache_data.get(key)
