class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0

        jump_count = [math.inf for _ in nums]
        jump_count[0] = 0

        for i, n in enumerate(nums):
            jump_index = i + n

            if jump_index >= len(nums) - 1:
                return jump_count[i] + 1
            for idx in range(i, jump_index + 1):
                jump_count[idx] = min(jump_count[idx], jump_count[i] + 1)

        return jump_count[-1]
