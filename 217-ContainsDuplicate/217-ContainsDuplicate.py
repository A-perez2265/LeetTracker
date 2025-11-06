# Last updated: 11/6/2025, 5:51:05 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:   # create an empty hashset
        hashset= set()
        # loop through nums
        for i in nums:
            if i in hashset:
                return True

            # add it to hashset with .add for sets
            hashset.add(i)
        return False
                