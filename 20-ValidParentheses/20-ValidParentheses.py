# Last updated: 8/24/2025, 1:24:19 AM
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
        return not stack
        