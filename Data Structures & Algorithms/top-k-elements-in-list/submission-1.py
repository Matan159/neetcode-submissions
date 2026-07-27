class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        output = []
        for _ in range(k):
            a = max(dic, key=dic.get)
            output.append(a)
            dic.pop(a)
        return output