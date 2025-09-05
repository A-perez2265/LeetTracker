# Last updated: 9/5/2025, 2:28:42 AM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstack = []
        for c in s:
            if c.isalnum():
                newstack += c.lower()
        return newstack == newstack[::-1]

        