from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sLetters = Counter(s)
        tLetters = Counter(t)
        for key in sLetters:
            if key not in tLetters or sLetters[key]!=tLetters[key]:
                return False
        return True