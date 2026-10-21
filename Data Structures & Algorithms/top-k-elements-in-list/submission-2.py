class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resDict = defaultdict(int)
        for num in nums:
            resDict[num] += 1
        pairs = []
        for num, value in resDict.items():
            pairs.append((num,value))
        pairs.sort(key=lambda item: item[1], reverse=True)
        res = []
        for i in range(k):
            res.append(pairs[i][0])
        return res