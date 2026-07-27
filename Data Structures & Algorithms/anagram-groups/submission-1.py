class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []

        def anagrams(s: str, t: str):
            if len(s) != len(t):
                return False
            dic = {}
            for cs in s:
                if cs in dic:
                    dic[cs] += 1
                else:
                    dic[cs] = 1
            for ct in t:
                if ct not in dic or dic[ct] == 0:
                    return False
                dic[ct] -= 1
            return True

        for st in strs:
            flag = False
            for stoutput in output:
                if anagrams(st, stoutput[0]):
                    stoutput.append(st)
                    flag = True
                    break
            if flag == False:
                output.append([st])
        return output