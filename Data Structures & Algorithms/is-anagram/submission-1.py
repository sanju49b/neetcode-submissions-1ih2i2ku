class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #using sorting
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        return False
        