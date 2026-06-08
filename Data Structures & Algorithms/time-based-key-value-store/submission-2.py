# Time Based Key-Value Store
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
# [irritating - AI]

class TimeMap:
    def __init__(self):
        # key -> (list of timestamps, list of values), both kept in sync
        self.times = defaultdict(list)
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""

        times = self.times[key]
        # binary search for the rightmost timestamp that is <= `timestamp`
        l, r = 0, len(times) - 1
        idx = -1
        while l <= r:
            m = (l + r) // 2
            if times[m] <= timestamp:
                idx = m          # candidate; look right for a larger valid one
                l = m + 1
            else:
                r = m - 1

        if idx == -1:
            return ""  # every stored timestamp is in the future
        return self.values[key][idx]
