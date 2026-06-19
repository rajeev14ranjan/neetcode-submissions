# Maximum Subarray
# Given an array of integers nums, find the subarray with the largest sum and return the sum.
# A subarray is a contiguous non-empty sequence of elements within an array.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        for n in nums:
            currSum += n
            maxSum = max(maxSum, currSum)
            currSum = max(currSum, 0)

        return maxSum
            