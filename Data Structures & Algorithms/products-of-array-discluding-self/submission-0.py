class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix= [0] * len(nums)
        ans= [0]* len(nums)
        for i in range(0,len(nums)):
            if i==0:
                prefix[i]=1
            else:
                prefix[i]=prefix[i-1]*nums[i-1]
                print(prefix[i])
        for i in range(len(nums)-1,-1,-1):
            if i== len(nums)-1:
                suffix[len(nums)-1]= 1
            else:
                suffix[i]=suffix[i+1]*nums[i+1]
                print(suffix[i])
        for i in range(0,len(nums)):
            ans[i]= suffix[i]* prefix[i]
        return ans