class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sLetters = {}
        for i in range(len(s)):
            if s[i] not in sLetters:
                sLetters[s[i]] = 1
            else:
                sLetters[s[i]] += 1
        for tChar in t:
            if tChar not in sLetters or sLetters[tChar] == 0:
                return False
            sLetters[tChar] -= 1

        return True