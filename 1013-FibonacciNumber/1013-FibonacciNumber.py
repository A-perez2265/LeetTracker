# Last updated: 8/26/2025, 8:56:43 PM
class Solution:
    def fib(self, n: int) -> int:
        ans = [0,1]

        for i in range(2,n+1):
            ans.append(ans[i-1] + ans[i-2])
        return ans[n]

        