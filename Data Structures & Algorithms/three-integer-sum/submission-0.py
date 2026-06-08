class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def check(nums,left,right,sumreq,result):
            if nums[p]+nums[q]== sumreq:
                result.append( [nums[i],nums[p+1],nums[q]])
                return True
            else:
                return False
        result= []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue    
                
            sumreq= -num
            p=i+1
            q= len(nums)-1

            while p<q:
                if nums[p]+ nums[q]== sumreq:
                    result.append([nums[i],nums[p],nums[q]])
                    p=p+1
                    q=q-1
                    while p < q and nums[p] == nums[p-1]:
                      p += 1

                    while p < q and nums[q] == nums[q+1]:
                        q -= 1
                elif nums[p]+nums[q] > sumreq:
                    q=q-1       
                else:
                    p=p+1
        return result
                


        