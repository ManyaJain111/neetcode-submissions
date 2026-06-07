import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right= max(piles)
        left=1
        while left<=right:
            mid=(right+left)//2
            count=0
            for pile in piles:
                count= count + math.ceil(pile/mid)
            
            if count>h:
                left=mid+1
            else:
                right= mid-1
        return left
        
            

            


        
        