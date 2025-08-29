# Last updated: 8/29/2025, 2:10:42 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for i, n in enumerate(nums):
            if n in map:
                return True
            else:
                map[n]=i
        return False
        

        