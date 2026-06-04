# Contains Duplicate
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for n in nums:
            if n in num_set: 
                return True
            else:
                num_set.add(n)
        
        return False
        