class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left = [1]*l
        right = [1]*l
        for i in range(1, l):
            left[i] *= left[i-1] * nums[i-1]
        for i in range(l-2, -1, -1):
            right[i] *= right[i+1] * nums[i+1]
        return [left[j]*right[j] for j in range(l)]
