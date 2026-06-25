# Minimum Interval to Include Each Query
# You are given a 2D integer array intervals, where intervals[i] = [left_i, right_i] represents the ith interval starting at left_i and ending at right_i (inclusive).
# You are also given an integer array of query points queries. The result of query[j] is the length of the shortest interval i such that left_i <= queries[j] <= right_i. If no such interval exists, the result of this query is -1.
# Return an array output where output[j] is the result of query[j].
# Note: The length of an interval is calculated as right_i - left_i + 1.
# ********* [simple brute force logic] *********

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda l: l[1]-l[0])
        ans = [-1] * len(queries)
        for qidx in range(len(queries)):
            for intv in intervals:
                if intv[0] <= queries[qidx] <= intv[1]:
                    ans[qidx] = (intv[1] - intv[0] + 1)
                    break
        
        return ans