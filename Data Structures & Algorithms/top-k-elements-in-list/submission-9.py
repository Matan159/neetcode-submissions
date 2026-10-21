class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies: O(N)
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # 2. Create buckets where index = frequency: O(N)
        # ⚠️ Must use list comprehension! Never use `[[]] * (len(nums) + 1)`
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # 3. Iterate backwards from highest possible frequency to 1: O(N)
        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res