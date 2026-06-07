import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        count= Counter(nums) # count= 1:3, 2:4...........
        for num,freq in count.items():
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                heapq.heappop(heap)
        result=[]
        for freq,num in heap:
            result.append(num)
        return result
        