from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        if not grid or not grid[0]:
            return
            
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        
        # 1. Multi-Source Initialization: Find ALL chests and add them to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c)) # The value at grid[r][c] is already 0
                    
        # 2. Run a SINGLE BFS
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                
                # Boundary check
                if 0 <= nr < rows and 0 <= nc < cols:
                    # If the current path offers a strictly shorter distance to this neighbor,
                    # update the neighbor and add it to the queue to keep exploring.
                    # (This automatically safely skips water cells and other chests)
                    if grid[r][c] + 1 < grid[nr][nc]:
                        grid[nr][nc] = grid[r][c] + 1
                        queue.append((nr, nc))