class Solution:
    
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            return self.myPow(1/x,-n)
        half = n//2
        if n%2==0:
            return self.myPow(x,half)*self.myPow(x,half)
        else:
            return self.myPow(x,half)*self.myPow(x,half) * x


        