# # Non-overlapping Intervals
# Given an array of intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Note: Intervals are non-overlapping even if they have a common point. For example, [1, 3] and [2, 4] are overlapping, but [1, 2] and [2, 3] are non-overlapping.
# ********** [counter intuitive][Greedy] **********

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        removal_count = 0

        prev = None

        print(intervals)

        for intv in intervals:
            # if it overlaps, intv start is before prev could end
            if prev and intv[0] < prev[1]:
                # we need to remove 1 from these 2 overlapping intervals
                removal_count += 1
                # ****** Greedy Algo - remove the 1 which ends early, the late ending interval will block more intervals
                prev = intv if intv[1] < prev[1] else prev
            else:
                prev = intv
        
        return removal_count

