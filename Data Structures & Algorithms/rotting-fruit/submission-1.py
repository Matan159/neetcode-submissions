from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        rotten = []
        flag = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append((i,j,0))
                elif grid[i][j] == 1:
                    flag = 1
        
        if flag == 0:
            return 0

        queue = deque(rotten)
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            r,c,minute = queue.popleft()
            for dr,dc in directions:
                nr = r+dr
                nc = c+dc
                if 0<=nr<rows and 0<=nc<cols:
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc,minute+1))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1

        return minute