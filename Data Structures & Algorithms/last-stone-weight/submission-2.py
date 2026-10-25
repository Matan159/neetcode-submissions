class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)
            to_push = a-b if a>b else b-a
            if to_push>0:
                heapq.heappush(heap, -to_push)
        return 0 if len(heap)==0 else -heap[0]