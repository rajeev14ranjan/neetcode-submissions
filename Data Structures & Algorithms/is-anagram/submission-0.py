class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        f_count = {}

        for ls, lt in zip(list(s), list(t)):
            f_count[ls] = f_count.get(ls, 0) + 1
            f_count[lt] = f_count.get(lt, 0) - 1

        highest_frequency = max(f_count.values())

        return highest_frequency == 0

        
        