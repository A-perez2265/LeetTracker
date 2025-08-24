# Last updated: 8/24/2025, 1:59:40 AM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        news= ""

        for c in s:
            if c.isalnum():
                news += c.lower()
        return news == news[::-1]
        