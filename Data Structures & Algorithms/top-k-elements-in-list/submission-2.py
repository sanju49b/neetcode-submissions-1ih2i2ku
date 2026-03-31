class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for num in nums:
            if num in seen:
                seen[num] +=1
            else:
                seen[num]=1
        # for using value to sort
        x = sorted(seen,key=lambda x: seen[x],reverse=True)
        return x[:k]
