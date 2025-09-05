# Last updated: 9/5/2025, 2:43:09 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(nums) == len(set(nums))