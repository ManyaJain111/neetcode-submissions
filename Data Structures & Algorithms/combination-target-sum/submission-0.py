class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def recurse(start,remaining,path):
            if remaining==0:
                res.append(path[:])
                return
            if remaining<0:
                return 
            for i in range(start,len(nums)):
                path.append(nums[i])
                recurse(i,remaining-nums[i],path)
                path.pop()
        recurse(0,target,[])
        return res
        

