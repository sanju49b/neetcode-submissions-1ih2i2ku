class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left+right) // 2
            if nums[middle] == target:
                return middle
            if nums[left] <= nums[middle]:
                # left part is sorted
                if nums[left] > target or target > nums[middle]:
                    left = middle + 1
                else:
                    right = middle
            else:
                if nums[right] < target or nums[middle] > target:
                    right = middle - 1
                else:
                    left = middle + 1
        return -1 