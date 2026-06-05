# Longest Consecutive Sequence
# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        res = 0
        for n in nums:
            # not a start of a seq
            if n-1 in numSet:
                continue
            
            #start of the seq
            length = 1
            while n+length in numSet:
                length += 1
            
            res = max(res, length)

        return res




