class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,val in enumerate(nums):
            # so we would geet the index and value
            # so once we get these
            x = target - val
            if x in hashmap.keys():
                return [hashmap[x],i]
                break
            hashmap[val] = i
