class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        concatinated = ""
        for s in strs:
            res = res+(str(len(s)))+','
            concatinated = concatinated+s
        return res+"*"+concatinated

    def decode(self, s: str) -> List[str]:
        lens = []
        c = s[0]
        i = 0
        num = ""
        while c != '*':
            while c!= ',':
                num = num + c
                i += 1
                c = s[i]
            lens.append(int(num))
            num = ""
            i += 1
            c = s[i]
        res = []
        i += 1
        for l in lens:
            res.append(s[i:i+l])
            i += l
        return res