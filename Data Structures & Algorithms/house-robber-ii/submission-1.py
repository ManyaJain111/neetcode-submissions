class Solution:
    def rob(self, nums: List[int]) -> int:
        dp ={}
        if len(nums)==1:
            return nums[0]
        first = nums[:-1]
        sec= nums[1:]
        def lessee(arr,i):
            if i in dp :
                return dp[i]
            if i>=len(arr):
                return 0
            take= arr[i] + lessee(arr,i+2)
            skip=  lessee(arr,i+1)
            dp[i]= max(take,skip)
            return dp[i]
        dp = {}
        ans1 = lessee(first,0)

        dp = {}
        ans2 = lessee(sec,0)

        return max(ans1, ans2)
        

        