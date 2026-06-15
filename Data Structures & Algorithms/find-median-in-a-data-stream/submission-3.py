# Find Median From Data Stream
# The median is the middle value in a sorted list of integers. For lists of even length, there is no middle value, so the median is the mean of the two middle values.

class MedianFinder:
    def __init__(self):
        # two heaps, right, left, minheap, maxheap
        # heaps should be equal size
        self.left, self.right = [], []

        # left ---|median|---right

    def addNum(self, num: int) -> None:
        left, right = self.left, self.right # to remove self.

        if right and num > right[0]:
            heapq.heappush(right, num)
        else:
            heapq.heappush(left, -1 * num)

        if len(left) > len(right) + 1:
            val = -1 * heapq.heappop(left)
            heapq.heappush(right, val)
        if len(right) > len(left) + 1:
            val = heapq.heappop(right)
            heapq.heappush(left, -1 * val)

    def findMedian(self) -> float:
        left, right = self.left, self.right # to remove self.

        if len(left) > len(right):
            return -1 * left[0]
        elif len(right) > len(left):
            return right[0]
        return (-1 * left[0] + right[0]) / 2.0