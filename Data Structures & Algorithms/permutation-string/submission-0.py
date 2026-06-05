class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        if not s1: return True

        start = 0
        s1dict = {}
        for s in s1:
            s1dict[s] = s1dict.get(s, 0) + 1

        bag = {}
        for end in range(len(s2)):
            bag[s2[end]] = bag.get(s2[end], 0) + 1

            if end - start + 1 > len(s1):
                if bag[s2[start]] == 1:
                    del bag[s2[start]]
                else:
                    bag[s2[start]] = bag.get(s2[start], 0) - 1
                start += 1

            if s1dict == bag:
                return True

        return False
