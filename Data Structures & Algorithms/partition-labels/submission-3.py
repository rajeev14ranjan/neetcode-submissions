# Partition Labels
# You are given a string s consisting of lowercase english letters.

# We want to split the string into as many substrings as possible, while ensuring that each letter appears in at most one substring.

# Return a list of integers representing the size of these substrings in the order they appear in the string.
# **** Better logic***

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}
        for i in range(len(s)):
            lastIdx[s[i]] = i

        farthest = 0
        length = 0
        result = []

        for i in range(len(s)):
            farthest = max(farthest, lastIdx[s[i]])
            length += 1

            if i == farthest:
                result.append(length)
                length = 0

        return result


        
