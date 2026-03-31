class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable={}
        for i,j in enumerate(nums):
            x = target - j
            if x in hashtable.keys():
                return [hashtable[x],i]
            else:
                hashtable[j]=i