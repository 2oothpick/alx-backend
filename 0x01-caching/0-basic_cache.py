#!/usr/bin/env python3
"""
Caching via a basic dictionary
"""

# import BaseCaching from base_caching.py
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Class inherits BaseCaching and overrides
    its put and get methods
    """

    def put(self, key, item):
        """
        Populates the self.cache_data dictionary
        """
        if key is not None or item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """
        Returns dictionary values for the provided key
        """
        if key in self.cache_data.keys() and key is not None:
            return self.cache_data.get(key)
        return None
