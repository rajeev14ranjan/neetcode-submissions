# Longest Repeating Character Replacement
# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.
# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        bag = {}
        ans = 0

        for end in range(len(s)):
            bag[s[end]] = bag.get(s[end], 0) + 1

            max_repeat_count = max(bag.values())

            # remove if invalid
            while (end - start + 1 - max_repeat_count) > k:
                # reduce
                if bag[s[start]] == 1:
                    del bag[s[start]]
                else:
                    bag[s[start]] -= 1

                start += 1

            # now the bag should be valid
            ans = max(ans, end - start + 1)

        return ans
