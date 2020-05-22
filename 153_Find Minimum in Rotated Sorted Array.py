class Solution(object):

    def findMin(self, nums):
        i, j = 0, len(nums) - 1
        while i < j - 1:
            m = i + (j - i) / 2
            if nums[i] < nums[j]:
                return nums[i]
            elif nums[i] > nums[m]:
                j = m
            else:
                i = m
        
        return min(nums[i], nums[j])
    
    def findMinBinary1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        i, j = 0, len(nums) - 1
        
        if nums[i] <= nums[j]: 
            return nums[i]
        
        while i <= j:
            m = i + (j - i) / 2
            if m == len(nums) - 1:
                return nums[m]
            elif nums[m] > nums[m + 1]:
                return nums[m + 1]
            elif nums[i] <= nums[m]:
                i = m + 1
            else:
                j = m - 1
        return nums[i]