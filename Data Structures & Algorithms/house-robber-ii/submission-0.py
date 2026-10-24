class Solution:
    def rob1(self, nums: List[int]) -> int:
        memo = { # keeps track of maximum money I could rob from start to and including house i
            0:nums[0], 1:max(nums[1],nums[0])
        }
        for i in range(2, len(nums)):
            memo[i] = max(nums[i]+memo[i-2], memo[i-1])
        return memo[len(nums)-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])
        return max(self.rob1(nums[1:]), self.rob1(nums[:-1]))