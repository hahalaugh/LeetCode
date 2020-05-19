class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        hold = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1] and hold == 0:
                hold = prices[i - 1]
            elif prices[i] < prices[i - 1] and hold > 0:
                total += (prices[i - 1] - hold)
                hold = 0
        
        if hold > 0:
            total += (prices[-1] - hold)
        
        return total


s = Solution()
#print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([1, 2, 3, 4, 5]))
