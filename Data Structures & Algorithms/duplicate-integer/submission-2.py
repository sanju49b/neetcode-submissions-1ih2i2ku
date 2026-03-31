class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # has to build a frequency hash map
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False