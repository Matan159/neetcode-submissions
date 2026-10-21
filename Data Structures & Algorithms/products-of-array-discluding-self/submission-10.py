class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1]*l
        resi = [1]*l
        for i in range(1, l):
            res[i] = res[i-1]*nums[i-1]
        for i in range(l-2, -1, -1):
            resi[i] = resi[i+1]*nums[i+1]
        for i in range(l):
            res[i] *= resi[i]
        return res