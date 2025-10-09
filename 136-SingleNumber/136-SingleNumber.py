# Last updated: 10/9/2025, 12:11:44 AM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map ={}

        for i in nums:
            if i not in map:
                map[i]=True
            elif i in map:
                map[i]=False
        for key,value in map.items():
            if value is True:
                return key  