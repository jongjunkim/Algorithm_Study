class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        row, col = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))

        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        
        count = 0
        while fresh > 0 and q:
            for k in range(len(q)):
                x,y = q.popleft()
                for dx, dy in directions:
                    i, j = x+dx, y+dy
                    if (i in range(row) and j in range(col) and grid[i][j] == 1):
                        grid[i][j] = 2 # wrong part == -> =
                        q.append((i,j))
                        fresh -= 1
            count += 1

        return count if fresh == 0 else -1