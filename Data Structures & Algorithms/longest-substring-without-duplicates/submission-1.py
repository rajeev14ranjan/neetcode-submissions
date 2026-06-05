# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.
# A substring is a contiguous sequence of characters within a string.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        
        l, r = 0, 1
        bag = set(s[l])
        ans = 1

        while l <= r < len(s):
            while r < len(s) and not s[r] in bag:
                bag.add(s[r])
                r += 1

            # s[r] is the duplicate char rn
            ans = max(ans, r - l)

            # now remove letters from bag to make space for s[r]
            while r < len(s) and s[r] in bag:
                bag.discard(s[l])
                l += 1

        return ans
