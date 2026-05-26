class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [0]*len(cost)
        cache[-1] = cost[-1]
        if len(cost) > 1:
            cache[-2] = cost[-2]
        else:
            return 0
        for i in range(len(cache)-3, -1, -1):
            cache[i] = cost[i] + min(cache[i+1], cache[i+2])
        print(cache)
        return min(cache[0], cache[1])