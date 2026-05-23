class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        # the length of the longest subarray
        longest = 0
        sett = set()
        n = len(s)
        #o(n)
        for r in range(n):
            #invalid condition
            #  o(n)
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            
            #valid window
            w = (r - l) + 1
            longest = max(longest,w)
            sett.add(s[r])
        
        return longest


        