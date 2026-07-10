class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp={}
        def money(i):
            if i>= len(cost):
                return 0
            if i in dp:
                return dp[i]
            dp[i]=cost[i]+ min(money(i+1),money(i+2))
            return dp[i]
        return min(money(0),money(1))


        