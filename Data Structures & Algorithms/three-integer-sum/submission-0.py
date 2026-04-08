class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums[i] + nums[j] + nums[k] == 0
        # we need to identify all the triplets
        # the approach is we have i using for 
        # and then we take a left and right pointer and we move them 
        # i previous elemeent shouldnt i-1
        # the same for left and right
        # and if i > 0 like 1 and then we can stop it then since l will be the next and we can never find 0


        #first we need to sort as we are going to squeeze
        nums.sort()

        n = len(nums)
        answer = []
        for i in range(n):
            if nums[i] > 0: #we wont be checking for postive numbers
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            
            #this is how we can iterate through elements like i can be the first element
            lo,hi = i+1,n-1
            while lo < hi:
                total = nums[i] + nums[hi] + nums[lo]
                if total == 0:
                    answer.append([nums[i], nums[hi],nums[lo]])
                    #to avoid duplicates
                    lo +=1
                    hi -=1
                    while lo<hi and nums[lo] == nums[lo-1]:
                        lo +=1
                    while lo<hi and nums[hi] == nums[hi+1]:
                        hi -=1
                elif total > 0:
                    hi-=1
                else:
                    lo+=1
        return answer
            
