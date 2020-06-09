class Solution(object):

    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for value in range(1, amount + 1):
               if value >= coin:
                   dp[value] += dp[value - coin]
        return dp[amount]
    
    def changeBottomUp2D(self, amount, coins):
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        dp[0][0] = 1
            
        for idx in range(1, len(coins) + 1):
            dp[idx][0] = 1
            for value in range(1, amount + 1):
                noUseLast = dp[idx - 1][value]
                useLast = 0 if value - coins[idx - 1] < 0 else dp[idx][value - coins[idx - 1]]
                dp[idx][value] = noUseLast + useLast
        return dp[-1][-1]
    
    def changeTopDown(self, amount, coins):
        d = {}
        
        def f(amount, idx):
            if idx < 0 or amount <= 0:
                return int(amount == 0)
            if (amount, idx) in d:
                return d[(amount, idx)]
            d[(amount, idx)] = f(amount - coins[idx], idx) + f(amount, idx - 1)
            return d[(amount, idx)]
            
        return f(amount, len(coins) - 1)


s = Solution()
print(s.change(7, [2, 3]))
