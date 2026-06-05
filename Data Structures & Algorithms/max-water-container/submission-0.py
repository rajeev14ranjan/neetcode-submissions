# Container With Most Water
# You are given an integer array heights where heights[i] represents the height of the
# ith bar.
# You may choose any two bars to form a container. Return the maximum amount of water a container can store.


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = 0

        l, r = 0, len(heights) - 1

        while l < r:
            lh = heights[l]
            rh = heights[r]
            water = max(water, (r - l) * min(lh, rh))

            if lh <= rh:
                l += 1
            else:
                r -= 1

        return water
