class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagrams(s,t):
            if len(s) != len(t):
                return False
            d = {}
            for i in range(len(s)):
                d[s[i]] = d.get(s[i], 0) + 1
                d[t[i]] = d.get(t[i], 0) - 1
            for _, j in d.items():
                if j != 0:
                    return False
            return True
        
        
        output = [[strs[0]]]
        for i in range(1, len(strs)):
            added_flag = False
            for j in range(len(output)):
                if isAnagrams(strs[i], output[j][0]):
                    output[j].append(strs[i])
                    added_flag = True
                    break
            if added_flag == False:
                output.append([strs[i]])
        return output