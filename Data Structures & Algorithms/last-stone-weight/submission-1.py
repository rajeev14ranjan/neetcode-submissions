# Last Stone Weight
# You are given an array of integers stones where stones[i] represents the weight of the ith stone.

# We want to run a simulation on the stones as follows:

# At each step we choose the two heaviest stones, with weight x and y and smash them togethers
#  - If x == y, both stones are destroyed
#  - If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# Continue the simulation until there is no more than one stone remaining.

# Return the weight of the last remaining stone or return 0 if none remain.


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones: return 0

        heap = [-s for s in stones] # max heap
        heapq.heapify(heap)

        while len(heap) > 1:
            s1 = heapq.heappop(heap)
            s2 = heapq.heappop(heap)

            sn = -abs(s1-s2)
            if sn != 0: heapq.heappush(heap, sn)

        return abs(heap[0]) if heap else 0