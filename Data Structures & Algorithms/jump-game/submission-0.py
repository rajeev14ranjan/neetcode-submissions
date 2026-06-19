class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxgoal = 0
        n = len(nums) - 1

        for i in range(n):
            maxgoal = max(maxgoal, i + nums[i])
            if i + 1 > maxgoal: return False
        
        return True