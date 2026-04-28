class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we need to return the targets index
        left = 0
        right = len(nums) - 1 
        while left <= right:
            middle = (left+right)//2
            if nums[middle] == target:
                return middle
            if nums[left] <= nums[middle]:
                #left is sorted
                if nums[left] <= target and nums[middle] >= target:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] <= target and target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1