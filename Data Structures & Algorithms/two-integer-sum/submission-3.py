class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        for i,num in enumerate(nums):
            freq[num]= i
        
        for i,num in enumerate(nums):
            compliment= target-num
            if compliment in freq and freq[compliment]!=i:
                return [i,freq[compliment]]
            
        
