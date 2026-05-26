class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k >= len(nums):
            return [max(nums)]
        if k == 1:
            return nums

        point_max = 0
        for i in range(1, k):
            if nums[i] > nums[point_max]:
                point_max = i
        res = [nums[point_max]]

        for i in range(k, len(nums)):
            if nums[i] >= nums[point_max]:
                point_max = i
                res.append(nums[point_max])
            elif i - point_max < k:
                res.append(nums[point_max])
            else:
                point_max = i-k+1
                for j in range(point_max, i + 1):
                    if nums[j] >= nums[point_max]:
                        point_max = j
                res.append(nums[point_max])

        return res