# Sliding Window Maximum
# You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.
# Return a list that contains the maximum element in the window at each step.
# ******* [Hard][Counter Intuitive] *******

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        
        mqueue = collections.deque()
        ans = []

        for i,n in enumerate(nums):
            # 1. REMOVE OUT-OF-BOUNDS:
            # Check the front of the deque. If the index stored there is no 
            # longer inside our current window, remove it.
            if mqueue and mqueue[0] <= i-k:
                mqueue.popleft()

            # 2. MAINTAIN MONOTONIC DECREASING ORDER:
            # Check the back of the deque. If the new current_val is greater than 
            # or equal to the values of the indices at the back, remove them.
            while mqueue and nums[mqueue[-1]] < n:
                mqueue.pop()

            # 3. ADD CURRENT:
            # Add the current index to the back of the deque.
            mqueue.append(i)

            # 4. RECORD MAXIMUM:
            # Once our window has reached size 'k' (index i >= k - 1), 
            # the maximum for the current window is ALWAYS at the front of the deque.
            if i >= k-1: # window size has reached, keep on removing now
                ans.append(nums[mqueue[0]])
        
        return ans
        