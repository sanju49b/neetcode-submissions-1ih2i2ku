class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # the concept of monotonic stack needs to be used here
        res =[0] * len(temperatures)
        stack = [] #this is a list of (temperature,index)
        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stacktemp,stackidx = stack.pop()
                res[stackidx] = i - stackidx
            stack.append([temp,i])
        return res
