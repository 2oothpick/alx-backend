#!/usr/bin/python3
"""
100-lfu_cache
"""
# import BaseCaching from base_caching.py

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Class inherits BaseCaching and overrides
    its put and get methods
    """

    def __init__(self):
        """
        Initializes the class
        """
        super().__init__()
        self.uses = dict()

    def put(self, key, item):
        """
        Populates the self.cache_data dictionary
        if key and item are not None.
        Deletes the least used item in the dictionary if
        the number of items exceed BaseCaching.MAX_ITEMS
        """
        if (key is None or item is None):
            return

        if (len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS
           and key not in self.cache_data.keys()):
            discard_key = min(self.uses, key=self.uses.get)
            del self.cache_data[discard_key]
            del self.uses[discard_key]
            print("DISCARD: {}".format(discard_key))
        if (key in self.cache_data.keys()):
            self.uses[key] += 1
        else:
            self.uses[key] = 1
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
