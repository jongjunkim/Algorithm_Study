class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # O(N*M)
        row, col = len(board), len(board[0])

        def dfs(i, j):

            if i < 0 or j < 0 or i >= row or j>= col or board[i][j] != "O":
                return

            board[i][j] = "P"
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(row):
            for j in range(col):            #if i is 0 or row-1
                 if board[i][j] == "O" and (i in [0, row - 1] or j in [0, col - 1]):
                    dfs(i, j)

        for i in range(row):
            for j in range(col):
                 if board[i][j] == "O":
                    board[i][j] = "X"

        for i in range(row):
            for j in range(col):
                if board[i][j] == "P":
                    board[i][j] = "O"