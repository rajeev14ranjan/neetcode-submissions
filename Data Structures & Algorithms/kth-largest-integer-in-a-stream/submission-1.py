# Kth Largest Element in a Stream
# Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.

# Implement the following methods:
# constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
# int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = nums[0:k]
        self.k = k
        heapq.heapify(self.pq)

        for i in range(k, len(nums)):
            if nums[i] > self.pq[0]:
                heapq.heappush(self.pq, nums[i])
                heapq.heappop(self.pq)

    def add(self, val: int) -> int:
        if len(self.pq) == self.k:
            if val > self.pq[0]:
                heapq.heappush(self.pq, val)
                heapq.heappop(self.pq)
        else:
            heapq.heappush(self.pq, val)
        
        return self.pq[0]
        
