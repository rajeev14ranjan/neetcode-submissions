# Jump Game

# You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.
# Return true if you can reach the last index starting from index 0, or false otherwise.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxgoal = 0
        n = len(nums) - 1

        for i in range(n):
            maxgoal = max(maxgoal, i + nums[i])
            if i + 1 > maxgoal: return False
        
        return True