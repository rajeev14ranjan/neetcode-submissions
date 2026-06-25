# Minimum Interval to Include Each Query
# You are given a 2D integer array intervals, where intervals[i] = [left_i, right_i] represents the ith interval starting at left_i and ending at right_i (inclusive).
# You are also given an integer array of query points queries. The result of query[j] is the length of the shortest interval i such that left_i <= queries[j] <= right_i. If no such interval exists, the result of this query is -1.
# Return an array output where output[j] is the result of query[j].
# Note: The length of an interval is calculated as right_i - left_i + 1.
# ********* [Optimized logic] *********

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort both in ascending order
        intervals.sort()

        d = {}
        mheap = []
        i = 0

        for q in sorted(queries):
            if q in d: continue # to handle duplicates val in queries 

            # add to heap all intervals which starts before or at q
            while i < len(intervals) and intervals[i][0] <= q:
                intv_len = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(mheap, (intv_len, intervals[i][1]))
                i += 1
            
            # remove from heap if the top answer - interval with min length 
            # doesn't overlap with heap. Note - there can be intervals which doesn't overlap in heap
            # but we are only concerned with the top answer. (filtering only on eligible ans and not on entire heap)
            while mheap and mheap[0][1] < q:
                heapq.heappop(mheap)

            # save the length for this q
            d[q] = mheap[0][0] if mheap else -1
        
        return [d[q] for q in queries]


