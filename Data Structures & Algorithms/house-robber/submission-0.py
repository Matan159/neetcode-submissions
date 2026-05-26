class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [0]*len(nums)
        cache[-1] = nums[-1]
        if len(nums) > 1:
            cache[-2] = max(nums[-1], nums[-2])
        else:
            return nums[0]
        for i in range(len(cache)-3, -1, -1):
            cache[i] = max(nums[i] + cache[i+2], cache[i+1])
        return cache[0]