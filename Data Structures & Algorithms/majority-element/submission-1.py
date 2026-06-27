# Majority Element
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times in the array. You may assume that the majority element always exists in the array.
# ********** [Another neat trick since majority # > n/2] **********

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = c = 0

        for n in nums:
            if c == 0: res = n
            c += (1 if res == n else -1)
        
        return res
        

