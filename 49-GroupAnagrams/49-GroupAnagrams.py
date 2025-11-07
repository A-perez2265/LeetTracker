# Last updated: 11/7/2025, 3:47:18 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c)-ord("a")] +=1
            res[tuple(count)].append(s)

        return list(res.values())
        