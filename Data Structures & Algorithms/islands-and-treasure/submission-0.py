from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return 


        def bfs(i, j, start_dis):
            queue = deque([(i,j,start_dis)])
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while queue:
                r, c, dist = queue.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if dist + 1 < grid[nr][nc]:
                            grid[nr][nc] = dist + 1
                            queue.append((nr, nc, dist + 1))

        
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    bfs(i, j, 0)

        return 