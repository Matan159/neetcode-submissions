class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        maxLs = [0] * l
        maxRs = [0] * l
        minBarHeight = [0] * l
        res = 0
        for i in range(1, l):
            maxLs[i] = max(maxLs[i-1], height[i-1])
        for i in range(l-2, 0, -1):
            maxRs[i] = max(maxRs[i+1], height[i+1])
        for i in range(l):
            minBarHeight[i] = min(maxLs[i], maxRs[i])
        for i in range(l):
            res += max(0, minBarHeight[i]-height[i])
        return res