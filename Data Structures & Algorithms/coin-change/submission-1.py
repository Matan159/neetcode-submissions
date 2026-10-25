class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helper(arr: List[int]) -> int:
            # Returns minimum in an array with default -1
            if len(arr) == 0:
                return -1
            return min(arr)

        memo = {0:0}
        options = []
        for i in range(1, amount+1):
            options.clear()
            for coin in coins:
                if i-coin in memo:
                    options.append(memo[i-coin]+1)
            if len(options) > 0:
                memo[i] = min(options)
        return -1 if amount not in memo else memo[amount]