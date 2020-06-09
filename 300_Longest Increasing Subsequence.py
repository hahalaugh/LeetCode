import bisect

class Solution(object):

    def lengthOfLIS(self, nums):
        lis = []
        for n in nums:
            idx = bisect.bisect_left(lis, n)
            if idx == len(lis):
                lis.append(n)
            else:
                lis[idx] = n
        
        return len(lis)
            
    def lengthOfLISON2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


s = Solution()
print(s.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
