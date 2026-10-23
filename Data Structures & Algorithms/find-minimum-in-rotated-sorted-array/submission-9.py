class Solution:
    def findMin(self, nums: List[int]) -> int:
        len_nums = len(nums)
        l, r = 0, len_nums-1
        while l <= r:
            m = l + ((r-l)//2)
            num1 = nums[m]
            num2 = nums[0] if m == len_nums-1 else nums[m+1]
            if num1 < num2:
                if nums[0] > num1:
                    r = m-1
                else:
                    l = m+1
            else:
                return num2
        return -1