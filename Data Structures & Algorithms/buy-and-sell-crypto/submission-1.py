class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxr = [0]*len(prices)
        for i in range(len(prices)-2, -1, -1):
            maxr[i] = max(maxr[i+1], prices[i+1])
        res = 0
        for i in range(len(prices)):
            res = max(res, maxr[i]-prices[i])
        return res