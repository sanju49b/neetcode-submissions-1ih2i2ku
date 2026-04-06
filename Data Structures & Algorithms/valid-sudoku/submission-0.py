class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we are given a 9 * 9 suduko box
        # we need to check for 3 checks
        # 1. Each row must contain the digits 1-9 without duplications
        # 2. Each column must contain the digits 1-9 without duplications
        # 3. Each of the nine 3 * 3 subboxes of the grid must contains 1-9 digits without duplications
        # rules to remember while suduko 
        # board[row][column]
        # i is row and j is column
        # case 1: board[i][j] --- row wise traversal 
        # for i in range(9)
        #   for j in range(9)
        #       print(board[i][j])
        # hashset for every single row for the entire grid
        # hashset for every column row for the entire column
        # hashet is used to represent each of the 3 * 3 grid
        # [4/3,4/3] = [1,1] this identifies which square they are part of
        # [2/3,2/3] = [0,0] that does unifly identify 

        #hasmap key is cols and values is the values
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sqaures = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in sqaures[(r//3,c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                sqaures[(r//3,c//3)].add(board[r][c])
        return True
