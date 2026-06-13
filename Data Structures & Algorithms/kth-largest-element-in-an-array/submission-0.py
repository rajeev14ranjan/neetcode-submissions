# Kth Largest Element in an Array
# Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.

# By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.

# Follow-up: Can you solve it without sorting? - yes

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[0:k]
        heapq.heapify(heap)

        for i in range(k, len(nums)):
            if nums[i] <= heap[0]: continue

            heapq.heappush(heap, nums[i])
            heapq.heappop(heap)
        
        return heap[0]