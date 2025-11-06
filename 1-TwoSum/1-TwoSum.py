# Last updated: 11/6/2025, 2:23:29 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in map:
                return [map[diff],i]
            else:
                map[n]=i
            
        