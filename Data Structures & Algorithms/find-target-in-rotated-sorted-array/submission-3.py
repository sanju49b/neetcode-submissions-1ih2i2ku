class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] >= nums[left]:
                #left sorted
                if nums[left] > target or target > nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                # right sorted array
                if nums[middle] > target or nums[right] < target:
                    right = middle - 1
                else:
                    left = middle + 1
        return -1