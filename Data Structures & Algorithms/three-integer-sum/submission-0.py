# 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort so we can skip duplicates and use the two-pointer scan.
        # O(n^2) time, O(1) extra space (ignoring the output).
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            # Once nums[i] > 0, (all positive value) no triplet can sum to zero (array is sorted).
            if nums[i] > 0:
                break
            # Skip duplicate anchors to avoid repeated triplets.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicates for the second and third elements.
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return result