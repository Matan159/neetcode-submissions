class Solution:
    def climbStairs(self, n: int) -> int:
        k = 0
        res = 0
        while n >= k:
            res += math.comb(n,k)
            n -= 1
            k += 1
        return res