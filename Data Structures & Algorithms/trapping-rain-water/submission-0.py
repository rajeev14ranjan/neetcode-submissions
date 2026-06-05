# Trapping Rain Water
# You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.
# Return the maximum area of water that can be trapped between the bars.


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxl, maxr = height[l], height[r]
        water = 0

        while l < r:
            effective_height = min(maxl, maxr)

            # left side water column
            water += max(effective_height - height[l], 0)

            # right side water column
            water += max(effective_height - height[r], 0)

            # updating maxl and maxr
            maxl, maxr = max(maxl, height[l]), max(maxr, height[r])

            if maxl < maxr:
                l += 1
            else:
                r -= 1

        return water

