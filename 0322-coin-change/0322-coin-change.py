class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # dp[i] = dp[i-num[i]] + num[i]
        dp = [float('inf')] * (amount+1)
        dp[0] = 0 #min num of coins needed
        coins = set(coins)
        # print(coins)
        for i in range(amount+1):
            for coin in coins:
                if i - coin >= 0: 
                    dp[i] = min(dp[i], dp[i-coin] + 1)
            # print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1