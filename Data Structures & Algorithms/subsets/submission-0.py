# Subsets
# Given an array nums of unique integers, return all possible subsets of nums.

# The solution set must not contain duplicate subsets. You may return the solution in any order.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # not adding ith elt
            dfs(i + 1, subset)

            # adding ith element
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()

        dfs(0, [])
        return res
