# Group Anagrams
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for str in strs:
            dkey = self.get_key(str)
            anagram_map.setdefault(dkey, []).append(str)

        return list(anagram_map.values())

    
    def get_key(self, str):
        key_dict = {}
        for s in list(str):
            key_dict[s] = key_dict.get(s, 0) + 1
    
        return frozenset(key_dict.items())

        