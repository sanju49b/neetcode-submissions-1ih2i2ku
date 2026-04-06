class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #the longestConsecutive probleem
        # can be solved with a hashset
        # and the main idea is to track the length for only number that dont have number-1 in the set
        # so we wont waste time computing for everything
        # lets start coding the solution up
        # when the num = num-1 not in hashset set that number to current
        # and then start length =1 and the while condition should be current+1 in hashset then update current and lenght
        # hashset with nums
        hashset = set(nums) #removes duplicates lookup is o(1)
        longest= 0
        for num in hashset:
            if num-1 not in hashset:
                current = num
                lenght = 1
                while current+1 in hashset:
                    current +=1
                    lenght +=1
                longest = max(longest,lenght)
        return longest
