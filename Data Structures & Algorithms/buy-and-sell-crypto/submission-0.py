class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minprice= float('inf')
        for price in prices:
            if price< minprice:
                minprice= price
            profit= max(profit,price-minprice)
        return profit


