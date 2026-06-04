# Two Sum
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = {}

        for i,n in enumerate(nums):
            if target - n in sum_map:
                return [sum_map[target-n], i]
            else:
                sum_map[n] = i

        return []

        