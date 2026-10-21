class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        chars = set(s[0])
        l, r = 0, 1
        res = 0
        while r < len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            r += 1
            res = max(res, len(chars))
        return res
        