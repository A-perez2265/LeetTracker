# Last updated: 8/29/2025, 2:16:34 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))