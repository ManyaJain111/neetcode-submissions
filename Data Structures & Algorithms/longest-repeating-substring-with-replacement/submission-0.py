class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq= {}
        left=0
        maxfreq=0
        res=0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0)+1
            maxfreq= max(maxfreq,freq[s[right]])
            while (right- left+1)- maxfreq>k:
                freq[s[left]]= freq[s[left]]-1
                left= left+1
            res= max(res,right-left+1)
        return res
        
        