class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[r]
        while l <= r:
            if nums[l]<nums[r]:
                return min(res, nums[l])
            if l == r-1:
                return min(nums[l], nums[r])
            m = l + ((r-l)//2)
            print("l:", l, ", m:", m, ", r:", r)
            res = min(res, nums[m])
            if nums[l] >= nums[m]:
                r = m - 1
            else:
                l = m + 1

        return res