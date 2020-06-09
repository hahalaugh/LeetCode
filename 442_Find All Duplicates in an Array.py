class Solution(object):

    def findDuplicates(self, nums):
        r = []
        for i in range(len(nums)):
            nums[abs(nums[i]) - 1] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                r.append(i + 1)
        return r


s = Solution()
print(s.findDuplicates([1, 2, 3, 2, 3, 4, 5]))
