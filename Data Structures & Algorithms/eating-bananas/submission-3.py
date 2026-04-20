class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # reading the question
        # you are given integer array piles
        # piles[i] is the number of bananas in the ith pile
        # we are also given integer h which represent the number of hours
        # we need to decide--k--which the speed of bananas the minimum integer
        def h_works(speed):
            # intial hours is obv zero
            hours = 0
            for i in piles:
                # we need to check each pile [i] and dive i / h
                # math.ceil gives us the smallest integer greater than or equal to x
                hours += math.ceil(i/speed)
            return hours <= h
        
        left = 1
        right = max(piles)
        # we are only trying to find the boundary
        while left < right:
            middle = (left+right)//2
            if h_works(middle):
                right = middle
            else:
                left = middle + 1
        return left