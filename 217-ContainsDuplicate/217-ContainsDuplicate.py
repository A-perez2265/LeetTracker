# Last updated: 8/29/2025, 2:17:07 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(nums) == len(set(nums))