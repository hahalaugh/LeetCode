class Solution:

    def countPrimes(self, n: int) -> int:
        nums = list(range(2, n))
        start = 0
        r = []
        while True:
            while start < len(nums) and nums[start] < 0:
                start += 1
            
            if start == len(nums):
                return len(r)
            
            r.append(nums[start])
            
            for i in range(start, len(nums), nums[start]):
                nums[i] = -abs(nums[i])

            
s = Solution()
print(s.countPrimes(2))
