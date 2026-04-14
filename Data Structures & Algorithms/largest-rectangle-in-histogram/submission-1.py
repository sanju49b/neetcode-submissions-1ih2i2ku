class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []
        maxArea = 0
        for i,height in enumerate(heights):
            start = i
            while stk and height < stk[-1][0]: 
                #(height,index)
                # heigh is less than the element at stack 
                # monotonic increasing order
                # like 2 is hiehgt 3 is element then 3 would break
                h , j = stk.pop()
                w = i - j
                a = h  * w
                maxArea = max(a,maxArea)
                start = j
            #for increasing order
            # this append would work in both cases to be honest
            # this would work even if the element is poped andd the eleme
            stk.append((height,start))
        
        #there might be stuff still on the stack
        while stk:
            height,idx = stk.pop()
            w = n - idx
            a = height * w
            maxArea = max(a,maxArea)
        
        return maxArea

    