class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #using Sorting     
        s=sorted(s)
        t=sorted(t)
        if s==t:
            return True
        return False