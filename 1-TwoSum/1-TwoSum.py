# Last updated: 9/5/2025, 2:46:10 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        stack = []

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in map:
                return map[diff],i
            else:
                map[n] = i
            
        