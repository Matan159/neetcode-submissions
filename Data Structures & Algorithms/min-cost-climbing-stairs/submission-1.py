class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {
            0:cost[0], 1:cost[1]
        }
        l = len(cost)
        for i in range(2, l):
            memo[i] = min(memo[i-1], memo[i-2]) + cost[i]
        return min(memo[l-1], memo[l-2])