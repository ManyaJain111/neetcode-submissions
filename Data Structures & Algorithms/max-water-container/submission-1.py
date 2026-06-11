class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left= 0
        right= len(heights)-1
        ans=-1
        while left<right:
            area = min(heights[left], heights[right]) * (right - left)
            ans = max(ans, area)
            if heights[right]>heights[left]:
                left= left+1
            elif heights[right]<=heights[left]:
                right= right-1

        return ans
