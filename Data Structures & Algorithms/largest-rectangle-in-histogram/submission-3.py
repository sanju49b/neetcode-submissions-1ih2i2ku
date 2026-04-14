class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #claculate length
        n = len(heights)
        stack = []
        area = 0
        for index,height in enumerate(heights):
            start = index
            #height is 2 and stack is 7 then we need to pop stack and then given the index of 7 to 2
            while stack and height < stack[-1][0]:
                h,idx = stack.pop()
                res = h * (index-idx)
                area = max(res,area)
                start = idx
            stack.append((height,start))
        
        while stack:
            ch,ci = stack.pop()
            ar = ch * (n-ci)
            area = max(area,ar)
        return area
            



