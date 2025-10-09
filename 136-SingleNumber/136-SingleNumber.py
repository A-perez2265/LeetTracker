# Last updated: 10/9/2025, 12:20:40 AM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)

        return seen.pop()
