# Merge Intervals
# Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# You may return the answer in any order.

# Note: Intervals are non-overlapping if they have no common point. For example, [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []

        for intv in intervals:
            prevIntv = ans[-1] if len(ans) else None
            # overlap
            if prevIntv and prevIntv[1] >= intv[0]:
                mergeIntv = [min(prevIntv[0], intv[0]), max(prevIntv[1], intv[1])]
                ans.pop()
                ans.append(mergeIntv)
            else:
                ans.append(intv)
        
        return ans