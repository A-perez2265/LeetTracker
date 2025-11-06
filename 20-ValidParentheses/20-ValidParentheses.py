# Last updated: 11/6/2025, 3:20:11 PM
class Solution:
    def isValid(self, s: str) -> bool:
        map = {')':'(',']':'[','}':'{'}
        stack = []

        for i in s:
            if i in map:
                if stack and stack[-1] == map[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return False if stack else True