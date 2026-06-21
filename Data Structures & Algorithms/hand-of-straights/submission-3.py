# Hand of Straights
# You are given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize.

# You want to rearrange the cards into groups so that each group is of size groupSize, and card values are consecutively increasing by 1.

# Return true if it's possible to rearrange the cards in this way, otherwise, return false.


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # total hands should be divisible into  n groups of groupSize each
        if len(hand) % groupSize > 0:
            return False

        freq = {}
        low = hand[0]
        for h in hand:
            freq[h] = freq.get(h, 0) + 1
            low = min(low, h)

        # start 1 by 1
        for h in hand:
            if h not in freq:
                continue

            low = h
            while low in freq:
                low -= 1

            # now low+1 is the begining, go for a groupSize
            for i in range(low + 1, low + 1 + groupSize):
                if i in freq and freq[i] > 0:
                    if freq[i] == 1:
                        del freq[i]
                    else:
                        freq[i] -= 1
                else:  # should not be possible as we don't have group
                    return False

        return True
