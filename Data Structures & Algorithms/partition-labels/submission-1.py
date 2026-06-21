# Partition Labels
# You are given a string s consisting of lowercase english letters.

# We want to split the string into as many substrings as possible, while ensuring that each letter appears in at most one substring.

# Return a list of integers representing the size of these substrings in the order they appear in the string.
# **** custom logic***


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = {}
        for l in s:
            freq[l] = freq.get(l, 0) + 1

        result = []
        left = right = 0
        curr = 0
        while right < len(s):
            l = s[right]
            # if this is a single letter, just add it to result
            if freq[l] == 1 and curr == 0:
                result.append(right - left + 1)
                left = right + 1
                right = right + 1
            else:
                # otherwise add the remaining letter to curr, and reduce it next time we see that letter
                curr += freq[l] - 1 if freq[l] > 0 else -1
                freq[l] = -1

                if curr == 0:  # i.e all the letter are completed
                    result.append(right - left + 1)
                    left = right + 1
                    right = right + 1
                else:
                    right += 1

        return result
