# Products of Array Except Self
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
# *** Without using division *****

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = [1]*n

        mul = 1
        for i in range(n):
            product[i] *= mul
            mul *= nums[i]
        
        mul = 1
        for i in range(n-1, -1, -1):
            product[i] *= mul
            mul *= nums[i]
        
        return product
