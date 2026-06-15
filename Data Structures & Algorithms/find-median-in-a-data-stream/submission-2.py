# Find Median From Data Stream
# The median is the middle value in a sorted list of integers. For lists of even length, there is no middle value, so the median is the mean of the two middle values.

class MedianFinder:
    def __init__(self):
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        small, large = self.small, self.large # to remove self.

        if large and num > large[0]:
            heapq.heappush(large, num)
        else:
            heapq.heappush(small, -1 * num)

        if len(small) > len(large) + 1:
            val = -1 * heapq.heappop(small)
            heapq.heappush(large, val)
        if len(large) > len(small) + 1:
            val = heapq.heappop(large)
            heapq.heappush(small, -1 * val)

    def findMedian(self) -> float:
        small, large = self.small, self.large # to remove self.

        if len(small) > len(large):
            return -1 * small[0]
        elif len(large) > len(small):
            return large[0]
        return (-1 * small[0] + large[0]) / 2.0