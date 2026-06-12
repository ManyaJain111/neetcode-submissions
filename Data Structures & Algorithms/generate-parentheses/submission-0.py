class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open=0
        close=0
        res=[]
        s="()"
        def recurse(n,path,s,open,close):
            
            if len(path)== n*2:
                res.append(path[:])
                return 
            if close<open:
                recurse(n,path+")",s,open,close+1)
            if open< n:
                recurse(n,path+"(",s,open+1,close)
       
        recurse(n,"",s,0,0)
        return res
            
            