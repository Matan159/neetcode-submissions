class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        output = []
        for _ in range(k):
            temp = max(d, key=d.get)
            d.pop(temp)
            output.append(temp)
        return output