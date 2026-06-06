# Largest Rectangle In Histogram
# You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

# Return the area of the largest rectangle that can be formed among the bars.

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left = [0]*len(heights) # how much ith bar can be extended to left (excluding ith)
        right = [0]*len(heights) # how much ith bar can be extended to right (excluding ith)

        stack = []
        for i,h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                idx = stack.pop()
                right[idx] = i-idx-1

            stack.append(i)
        
        # handle the reamining elements
        while stack:
            idx = stack.pop()
            right[idx] = len(heights) - idx - 1
        
        # now populate the left extension
        stack = []
        for j in range(len(heights)-1, -1, -1):
            while stack and heights[j] < heights[stack[-1]]:
                idx = stack.pop()
                left[idx] = idx - j -1
            stack.append(j)

        # handle the reamining elements
        while stack:
            idx = stack.pop()
            left[idx] = idx

        maxarea = 0
        for i in range(len(heights)):
            maxarea = max(maxarea, heights[i]*(left[i]+right[i]+1))

        return maxarea

        
        
