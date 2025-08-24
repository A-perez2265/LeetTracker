# Last updated: 8/24/2025, 1:58:03 AM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""

        for c in s:
            if c.isalnum():
                newString += c.lower()
        return newString == newString[::-1]

        