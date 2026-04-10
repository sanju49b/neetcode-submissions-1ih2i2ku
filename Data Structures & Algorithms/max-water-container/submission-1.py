class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left,right = 0,n-1
        result = 0
        for i in range(n):
            while left < right:
                water = min(heights[left],heights[right]) * (right-left)
                result = max(result,water)
                if heights[left] < heights[right]:
                    left += 1
                else:
                    right -=1
        return result