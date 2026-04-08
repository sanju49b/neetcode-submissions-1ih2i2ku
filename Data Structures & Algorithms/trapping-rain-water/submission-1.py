class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        result = []
        for i in range(n):
            left = max(height[0:i+1])
            right = max(height[i:n])
            water = max(0,min(left,right) - height[i])
            result.append(water)
        return sum(result)