# Last updated: 8/27/2025, 10:46:21 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for c in s:
            if c.isalnum():
                newString += c.lower()
        return newString == newString[::-1]

        