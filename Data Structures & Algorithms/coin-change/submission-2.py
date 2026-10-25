class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0} # used for memoization
        options = [] # used for keeping all options to get to a certain amount
        for i in range(1, amount+1): # bottom up approach
            options.clear()
            for coin in coins: # for each coin check if possible to get to amount with a single coin
                if i-coin in memo:
                    options.append(memo[i-coin]+1) # if possible then add to options
            if len(options) > 0:
                memo[i] = min(options) # if there are options to get to the amount, take the minimum
        return -1 if amount not in memo else memo[amount] # if there is no way to get to amount then return -1