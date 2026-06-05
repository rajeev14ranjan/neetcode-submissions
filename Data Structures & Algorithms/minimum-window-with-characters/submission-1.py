# Minimum Window Substring
# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".
# You may assume that the correct output is always unique.


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or len(s) < len(t):
            return ""

        tdict = {}
        for ch in t:
            tdict[ch] = tdict.get(ch, 0) + 1

        bag = {}
        start = 0
        ans = ""
        ans_len = len(s)

        for end in range(len(s)):
            bag[s[end]] = bag.get(s[end], 0) + 1

            # while the window in s includes t, shorten it
            while all(k in bag and bag[k] >= v for k, v in tdict.items()):
                # record
                if ans_len >= end - start + 1:
                    ans = s[start : end + 1]
                    ans_len = end - start + 1

                # remove start
                if bag[s[start]] == 1:
                    del bag[s[start]]
                else:
                    bag[s[start]] -= 1
                start += 1

        return ans
