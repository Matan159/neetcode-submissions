class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1]*m]*n
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                grid[i][j] = grid[i+1][j] + grid[i][j+1]
        return grid[0][0]