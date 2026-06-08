class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bsearch(l, r):
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        # finding pivot
        l, r, pivot_idx = 0, len(nums) - 1, -1
        if nums[0] < nums[-1] or len(nums) < 2:
            return bsearch(l, r)
        else:
            while l <= r:
                m = (l + r) // 2

                if nums[m] < nums[m - 1]:
                    pivot_idx = m
                    break
                elif nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        if pivot_idx == -1:
            return pivot_idx

        i = bsearch(0, pivot_idx - 1)

        return i if i >= 0 else bsearch(pivot_idx, len(nums) - 1)
