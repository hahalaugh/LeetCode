class Solution:

    def rob(self, nums):
        if not nums: return 0
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][i] = nums[i]
        
        for step in range(1, len(nums)):
            for i in range(0, len(nums) - step):
                j = i + step
                if step == 1:
                    dp[i][j] = max(dp[i][i], dp[j][j])
                elif 1 < step < len(nums) - 1:
                    dp[i][j] = max(dp[i][j - 2] + nums[j], dp[i][j - 1])
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return dp[0][-1]

    
s = Solution()
print(s.rob([2, 3, 2]))
print(s.rob([1, 2, 3, 1]))
