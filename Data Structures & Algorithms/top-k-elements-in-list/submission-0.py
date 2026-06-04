# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements within the array.

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = {}

        for num in nums:
            freq_count[num] = freq_count.get(num, 0) + 1
        
        pq = []

        for n,p in freq_count.items():
            heapq.heappush(pq, (-p, n))
        
        ans = []

        for _ in range(k):
            _, n = heapq.heappop(pq)
            ans.append(n)

        return ans
        