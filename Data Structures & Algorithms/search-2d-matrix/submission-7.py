class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # the trick is here is simple 
        # one thing we need to convert or think it in a 1d array
        # get columns and row
        # and in arr[m] , think of how m can be manipulated to give
        # row and column number with m // n , m % n
        # to get the right row and column we need to check
        row = len(matrix)
        column = len(matrix[0])
        n  = row * column
        left = 0
        right = n - 1
        while left <= right:
            middle = (left+right)//2
            value = matrix[middle//column][middle%column]
            if target == value:
                return True
            elif value > target: 
                right = middle - 1
            else:
                left = middle + 1
        return False