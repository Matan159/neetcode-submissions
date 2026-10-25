class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return math.sqrt(x**2 + y**2)

        heap = [(dist(p[0], p[1]), i) for i, p in enumerate(points)]
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            idx = heapq.heappop(heap)[1]
            res.append(points[idx])
        return res