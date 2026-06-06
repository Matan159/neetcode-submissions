import copy
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        res = [['X']*cols for _ in range(rows)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = []
        for i in range(cols):
            if board[0][i] == 'O':
                queue.append((0,i))
                res[0][i] = 'O'
            if board[rows-1][i] == 'O':
                queue.append((rows-1,i))
                res[rows-1][i] = 'O'
        for i in range(1, rows-1):
            if board[i][0] == 'O':
                queue.append((i,0))
                res[i][0] = 'O'
            if board[i][cols-1] == 'O':
                queue.append((i,cols-1))
                res[i][cols-1] = 'O'
        
        def dfs(r,c):
            for dr, dc in directions:
                nr = dr+r
                nc = dc+c
                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] == 'O' and res[nr][nc] == 'X':
                        res[nr][nc] = 'O'
                        dfs(nr,nc)
        
        for r,c in queue:
            dfs(r,c)

        board[:] = res