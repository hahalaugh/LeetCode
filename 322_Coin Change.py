class Solution(object):
    def coinChange(self, coins, amount):
        # Bottom Up
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for c in coins:
            for n in range(c, amount + 1):
                dp[n] = min(dp[n], dp[n - c] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
                
    def coinChangeTopDown(self, coins, amount):
        #Top Down
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        d = {}
        for c in coins:
            d[c] = 1
        
        def cal(amount):
            if amount in d:
                return d[amount]
            
            if amount < 0:
                return -1
            
            if amount == 0:
                return 0
            
            if amount in coins:
                return 1

            mi = float('inf')
            for c in coins:
                result = cal(amount - c) + 1
                if result > 0 and result < mi:
                    mi = result
            d[amount] = mi
            return d[amount]
        
        res = cal(amount)
        return res if res != float('inf') else -1
    