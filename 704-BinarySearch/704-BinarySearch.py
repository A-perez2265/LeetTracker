# Last updated: 8/27/2025, 1:00:25 AM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1 


        while low <= high:
            mid = (low + high) //2 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid -1 
        return -1 
        