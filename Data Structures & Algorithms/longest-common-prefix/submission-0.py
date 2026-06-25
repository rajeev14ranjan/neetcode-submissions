class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""

        cp = strs[0]

        for i in range(1, len(strs)):
            s = strs[i]
            
            i = min(len(cp), len(s))
            while i > 0 and cp[:i] != s[:i]:
                i -= 1
            if i == 0: return ""

            cp = cp[:i]
        
        return cp





