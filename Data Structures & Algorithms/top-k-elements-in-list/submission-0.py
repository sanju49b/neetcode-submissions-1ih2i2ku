class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1 , construct a hashmap first
        #2 , sort the hashmap based on the freq by using .items()
        #3 , gives the frequency as a List


        # constructing hashmap
        hashmap={}
        for i in nums:
            if i in hashmap:
                hashmap[i] +=1
            else:
                hashmap[i] = 1
        
        # this constructs the hashmap
        # sort
        sorted_values = sorted(hashmap.items(),key=lambda x: x[1], reverse=True)
        output = []
        for i in sorted_values[:k]:
            output.append(i[0])
        return output