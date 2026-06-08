# Koko Eating Bananas
# You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.
# You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.
# Return the minimum integer k such that you can eat all the bananas within h hours.

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # valid range of k -> [1, max(piles)] as h is >= len(piles)
        
        if len(piles) == h: return r # all piles within a day
        
        ans = r
        while l <= r:
            k = (l + r) // 2 # start with the middle val as k
            t = sum([math.ceil(p/k) for p in piles])
            
            if t <= h: # took less or equal time
                ans = min(ans, k) # record as this is a valid case
                r = k - 1  # but still reduce k to see if minimum exists
            else:
                l = k + 1  # took more or equal time, increase speek k (this will help in getting min)     
            
        return ans

