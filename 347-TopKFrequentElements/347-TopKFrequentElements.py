# Last updated: 11/8/2025, 4:50:52 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        counts = Counter(nums)
    
        min_heap = []
    
        for num, freq in counts.items():
            heapq.heappush(min_heap, (freq, num))
        
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        result = []
        for item_tuple in min_heap:
            freq = item_tuple[0]  
            num = item_tuple[1]  
            result.append(num)   
    
        return result
        