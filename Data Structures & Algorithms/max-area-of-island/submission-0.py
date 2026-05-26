class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def dfs(i,j):
            if 0<=i<rows and 0<=j<cols and grid[i][j] == 1:
                grid[i][j] = 2
                return 1 + dfs(i+1, j)+dfs(i, j+1)+ dfs(i-1, j)+ dfs(i, j-1)
            return 0

        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res = max(res, dfs(i,j))
                          
        return res 