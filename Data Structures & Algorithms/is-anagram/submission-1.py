class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        freq2={}
        if len(s)!=len(t):
            return False
        for num in s :
            freq[num]= freq.get(num,0)+ 1
        for num in t :
            freq2[num]= freq2.get(num,0)+ 1
        for num in s:
           if freq.get(num,0)!= freq2.get(num,0):
            return False
        return True

        
        