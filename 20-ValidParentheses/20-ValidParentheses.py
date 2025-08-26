# Last updated: 8/25/2025, 10:53:33 PM
class Solution:
    def countBits(self, n: int) -> List[int]:
        stack = []

        for k in range(n+1):
            binary = bin(k)
            count = 0
            for i in binary:
                if i == '1':
                    count += 1
            stack.append(count)
        return stack

                    

        