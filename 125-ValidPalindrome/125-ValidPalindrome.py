# Last updated: 8/27/2025, 10:47:08 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for i in s:
            if i.isalnum():
               new = new + i.lower()   

        return True if new == new[::-1] else False
     