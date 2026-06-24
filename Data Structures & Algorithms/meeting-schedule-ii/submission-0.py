"""
Meeting Rooms II
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of rooms required to schedule all meetings without any conflicts.
Note: (0,8),(8,10) is NOT considered a conflict at 8.

Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

# *********[solved using sweeping line algorithm]********
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        map = defaultdict(int) # use map instead of array -> much cleaner

        for i in intervals:
            map[i.start] += 1
            map[i.end] -= 1
        
        room_count, running_sum = 0, 0
        for _, v in sorted(map.items()):
            running_sum += v
            room_count = max(room_count, running_sum)
        
        return room_count
