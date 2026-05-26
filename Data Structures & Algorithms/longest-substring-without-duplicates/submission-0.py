class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = 1
        curr = 1
        substring = set(s[0])
        left = 0
        right = 1
        while right<len(s):
            while s[right] in substring:
                substring.remove(s[left])
                left += 1
                curr -= 1
            substring.add(s[right])
            right += 1
            curr += 1
            res = max(res, curr)
        return res