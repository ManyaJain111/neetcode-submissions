import heapq
class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        minheap=[]
        for stone in stones:
            heapq.heappush(minheap,-stone)
            
        if len(minheap)==1:
            return -minheap[0]
        else:
            while len(minheap)>1:
                least=- heapq.heappop(minheap)
                print("least")
                print(least)
                secleast= -heapq.heappop(minheap)
                print("sec")
                print(secleast)
                if least!= secleast:
                    heapq.heappush(minheap,-abs(least-secleast))
                    
        return -minheap[0] if minheap else 0
        
        


        