class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right= len(nums)-1
        def serchhh(nums,target,left,right):
            mid= (right+left)//2
            if left>right:
                return -1
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                return serchhh(nums,target,mid+1,right)
            else:
                return serchhh(nums,target,0,mid-1)

        return serchhh(nums,target,left,right)   