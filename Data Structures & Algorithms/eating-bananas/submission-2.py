class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            return hours <= h
        
        l = 1
        r = max(piles)
        while l < r:
            middle =  (l+r)//2
            if k_works(middle):
                r = middle 
            else:
                l = middle + 1
        return l

