class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #the question is we need to fix prefix and postfix using i and j
        #and we create two arrays and multiply them
        n = len(nums)
        prefix= [0] * n
        suffix = [0] * n
        pre_l = 1
        suff_r =1
        for i in range(n):
            j = -i-1
            prefix[i] = pre_l
            suffix[j] = suff_r
            pre_l *= nums[i]
            suff_r *= nums[j]
        return [l*r for l,r in zip(prefix,suffix)]
