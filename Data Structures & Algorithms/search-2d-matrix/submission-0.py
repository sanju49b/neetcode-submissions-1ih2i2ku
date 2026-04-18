class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # [[1,3,5,7],[10,11,16,20],[23,30,40,60]]
        # the target we are looking for 13
        # say this is a long vector like flatten it out
        # m = 3 and n = 4 and t = 3 * 4, t = 12
        # m is number of rows and n is number columns
        # 0 1 2 3 
        # 4 5 6 7
        # 8 9 10 11
        # flattening it out
        # l = 0 and r = 11 and m = 5 and element is 11 and this is fake index and this is just imagination
        # we generally need (i,j) where i is the row number and j is column number
        # so 11 doesnt work out
        # 1 3 5 7 #0
        # 10 11 16 20 #1
        # 23 30 34 60 #2
        # 0   1  2  3
        # i = m // n  , 5 // 4 = [1] -- row index
        # j = m % n , 6 % 4 = [2] -- column index
        # row index = m // n , number of rows/ number of columns
        # column index = m % n,  for the column index
        # value = mat[i][j]
        #number of elements
        n = len(matrix[0])
        t = len(matrix) * len(matrix[0])
        #flattend versions
        l = 0
        r = t-1
        while l <= r:
            m = (l+r) //2

            i = m // n
            j = m % n

            mid_num = matrix[i][j]

            if target == mid_num:
                return True
            elif target < mid_num:
                r = m - 1
            else:
                l = m + 1
        return False



