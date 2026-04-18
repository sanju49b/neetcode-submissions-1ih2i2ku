class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # so the trick here is to think the answer as 1d array right
        # so 1,2,4,8,10,11,12,13,14,20,30,40
        rows , columns = len(matrix),len(matrix[0])
        l = 0
        n = rows * columns
        r = n - 1
        while l <= r:
            middle = (l + r) // 2
            i,j = middle//columns,middle%columns
            mid_num =  matrix[i][j]
            if mid_num  == target:
                return True
            elif mid_num > target:
                r = middle - 1
            else:
                l = middle + 1
        return False