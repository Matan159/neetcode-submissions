import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-x for x in stones]
        heapq.heapify(s)
        while len(s) > 1:
            a = heapq.heappop(s)
            b = heapq.heappop(s)
            heapq.heappush(s, -abs(a-b))
            print(s)
        return -s[0]