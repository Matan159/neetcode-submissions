class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right = [1]*len(nums)
        for i in range(1, len(left)):
            left[i] *= left[i-1] * nums[i-1]
        for i in range(len(right)-2, -1, -1):
            right[i] *= right[i+1] * nums[i+1]
        print(left)
        print(right)
        return [left[j]*right[j] for j in range(len(nums))]
