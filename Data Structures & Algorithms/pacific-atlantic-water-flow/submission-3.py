from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pac_reachable = set()
        atl_reachable = set()

        def dfs(r, c, reachable_set, prev_height):
            # Stop if out of bounds, already visited, or strictly lower than the previous cell
            if (r < 0 or c < 0 or r == rows or c == cols or
                (r, c) in reachable_set or heights[r][c] < prev_height):
                return
                
            # Mark as reachable from this ocean
            reachable_set.add((r, c))
            
            # Search all 4 directions
            dfs(r + 1, c, reachable_set, heights[r][c])
            dfs(r - 1, c, reachable_set, heights[r][c])
            dfs(r, c + 1, reachable_set, heights[r][c])
            dfs(r, c - 1, reachable_set, heights[r][c])

        # 1. Start searches from the top and bottom rows
        for c in range(cols):
            dfs(0, c, pac_reachable, heights[0][c])               # Top edge (Pacific)
            dfs(rows - 1, c, atl_reachable, heights[rows - 1][c]) # Bottom edge (Atlantic)

        # 2. Start searches from the left and right columns
        for r in range(rows):
            dfs(r, 0, pac_reachable, heights[r][0])               # Left edge (Pacific)
            dfs(r, cols - 1, atl_reachable, heights[r][cols - 1]) # Right edge (Atlantic)

        # 3. Find the intersection
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac_reachable and (r, c) in atl_reachable:
                    res.append([r, c])
                    
        return res