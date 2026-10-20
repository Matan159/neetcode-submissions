class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i, n in enumerate(nums):
            numDict[n] = i
        for i, n in enumerate(nums):
            diff = target - n
            if diff in numDict and numDict[diff]!=i:
                return [i, numDict[diff]]
        return []