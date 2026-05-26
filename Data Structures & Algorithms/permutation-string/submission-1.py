class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        def isPermutation (st1, st2):
            st2 = "".join(sorted(st2))
            for i in range(len(st1)):
                if st1[i] != st2[i]:
                    return False
            return True
        
        l = len(s1)
        s1 = "".join(sorted(s1))
        for i in range(len(s2)-l+1):
            if isPermutation(s1, s2[i:i+l]):
                return True
        return False