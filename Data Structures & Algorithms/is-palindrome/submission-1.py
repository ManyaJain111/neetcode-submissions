class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right= len(s)-1
        s= s.lower()
        while left<=right:
            if not s[left].isalnum():
                left= left+1
                continue
            if not s[right].isalnum():
                right= right -1   
                continue
            if s[left]==s[right]:
                left=left+1
                right=right-1
            else:
                return False
        return True
            


           

        