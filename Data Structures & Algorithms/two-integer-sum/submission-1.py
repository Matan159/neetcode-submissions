class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdic = {}
        for i in range(len(nums)):
            numdic[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in numdic and i != numdic[target - nums[i]]:
                return [i, numdic[target - nums[i]]]