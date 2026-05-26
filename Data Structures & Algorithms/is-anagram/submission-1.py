class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = {}
        for cs in s:
            if cs in a:
                a[cs] += 1
            else:
                a[cs] = 1
        for ct in t:
            if ct not in a or a[ct] == 0:
                return False
            else:
                a[ct] -= 1
        return True