# Products of Array Except Self
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_indices = set()
        for i in range(len(nums)):
            if nums[i] != 0:
                product = product * nums[i]
            else:
                zero_indices.add(i)

        ans = []

        for i in range(len(nums)):
            if nums[i] == 0:
                ans.append(product if len(zero_indices) == 1 else 0)
            else:
                ans.append(int(product/nums[i]) if len(zero_indices) == 0 else 0)

        return ans