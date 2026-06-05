# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.
# A substring is a contiguous sequence of characters within a string.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        
        start = 0
        bag = set()
        ans = 0

        for end in range(len(s)):
            end_char = s[end]
            if end_char in bag:
                while end_char in bag:
                    bag.discard(s[start])
                    start += 1
            
            bag.add(end_char)
            ans = max(ans, end - start + 1)
        
        return ans
