# Find Minimum in Rotated Sorted Array
# You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.
# Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if array is rotated n times, resulting in original array then
        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]

        # array is rotated, we need to find a number whose left is greater than that number
        l, r = 1, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m - 1] > nums[m]:
                return nums[m]
            elif nums[m] > nums[0]: # the first no is the key, half of the array is greater than first no and rest of the half less.
                l = m + 1
            else:
                r = m - 1

        return nums[0]  # shouldn't hit
