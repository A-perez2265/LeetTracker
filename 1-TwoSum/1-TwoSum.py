# Last updated: 8/20/2025, 1:32:13 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # stores val and index

        for i,n in enumerate(nums):
            diff = target - n 
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n]=i
        return 