# Last updated: 11/7/2025, 4:19:40 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for s in nums:
            if s in freq:
                freq[s] += 1
            else:
                freq[s] = 1
        all_items =list(freq.items())

        sorted_list = sorted(all_items , key=lambda item: item[1], reverse=True)

        k_top_items = sorted_list[:k]

        result = []

        for item in k_top_items:
            result.append(item[0])
        return result
        