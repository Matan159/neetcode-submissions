
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = [[i, 0] for i in range(len(points))]
        for i, point in enumerate(points):
            dis[i][1] = math.sqrt((point[0])**2 + (point[1])**2)

        dis.sort(key = lambda x: x[1])

        res = []
        for i in range(k):
            res.append(points[dis[i][0]])
        
        return res