class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        row, col = len(grid), len(grid[0])
        maxisland = 0

        def dfs(i, j):

            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] != 1:
                return 0

            grid[i][j] = '0'
            res = 1
            res += dfs(i+1, j)  
            res += dfs(i-1, j) 
            res += dfs(i, j+1) 
            res +=  dfs(i, j-1)
           
            return res
           
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    maxisland = max(maxisland, dfs(i, j))

        return maxisland