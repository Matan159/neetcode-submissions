from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resDict = {}
        for word in strs:
            anagramKey = [0]*26
            for char in word:
                index = ord(char)-ord('a')
                anagramKey[index] += 1
            aKeyTup = tuple(anagramKey)
            if aKeyTup in resDict:
                resDict[aKeyTup].append(word)
            else:
                resDict[aKeyTup] = [word]
        res = []
        for group in resDict.values():
            res.append(group)
        return res