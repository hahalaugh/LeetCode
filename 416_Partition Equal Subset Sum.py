class Solution(object):

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2 == 1:
            return False
        
        capacity = sum(nums) / 2
        d = {}
        
        def load(i, capacity):
            if i == 0:
                return nums[i] == capacity
            elif (i, capacity) in d:
                return d[(i, capacity)]
            else:
                d[(i, capacity)] = load(i - 1, capacity - nums[i]) or load(i - 1, capacity)
                return d[(i, capacity)]
        
        return load(len(nums) - 1, capacity)


s = Solution()
print(s.canPartition([1, 5, 11, 5]))
