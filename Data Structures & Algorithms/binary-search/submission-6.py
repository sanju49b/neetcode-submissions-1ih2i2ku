class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # the problem is asking us to write binary search algorithm
        left = 0
        n = len(nums)
        right = n - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1