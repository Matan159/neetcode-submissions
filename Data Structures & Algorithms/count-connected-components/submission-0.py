class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0
        if len(edges) == 0:
            return n

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = [0]*n
        q = deque([])
        res = 0
        while sum(visit) < n:
            for i in range(n):
                if visit[i] == 0:
                    visit[i] = 1
                    q.append((i,-1))
                    break
            res += 1

            while q:
                node, parent = q.popleft()
                for nei in adj[node]:
                    if nei == parent:
                        continue
                    if visit[nei] == 0:
                        visit[nei] = 1
                        q.append((nei, node))

        return res