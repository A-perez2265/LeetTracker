# Last updated: 8/24/2025, 10:47:17 PM
class Solution:
    def isValid(self, s: str) -> bool:
        map = {')':'(',']':'[','}':'{'}
        stack = []

        for c in s:
            if c in map:
                if stack and stack[-1] == map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        