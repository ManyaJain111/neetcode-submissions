class Solution:
    def rob(self, nums: List[int]) -> int:
        dp={}
        def lessee(i):
            if i in dp:
                return dp[i]
            if i >=len(nums):
                return 0
            take = nums[i]+lessee(i+2)
            skip= lessee(i+1)
            dp[i]= max(take,skip)
            return dp[i]
        return lessee(0)