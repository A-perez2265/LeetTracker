# Last updated: 8/22/2025, 11:39:48 PM
class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {'(':')','[':']','{':'}'}
        stack = []

        for char in s:
            if char in hmap:
                stack.append(char)
            elif char in hmap.values():
                if stack and char == hmap[stack[-1]]:
                    stack.pop()
                else:
                    return False 
        return not stack

        
        