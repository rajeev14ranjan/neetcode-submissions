# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements within the array.

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        char_count = {}

        for num in nums:
            char_count[num] = char_count.get(num, 0) + 1
        
        min_heap = []

        for n,p in char_count.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (p, n))
            elif p > min_heap[0][0]: # filter before sink method
                    heapq.heappush(min_heap, (p, n))
                    heapq.heappop(min_heap) # to maintain only K elements
            else:
                continue # alreay top k selects

        return [num for count, num in min_heap]
        