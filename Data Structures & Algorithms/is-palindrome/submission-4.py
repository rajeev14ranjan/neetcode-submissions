class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two-pointer scan from both ends — O(n) time, O(1) space.
        l, r = 0, len(s) - 1
        while l < r:
            # Skip non-alphanumeric characters on either side.
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            # Compare characters case-insensitively.
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True
