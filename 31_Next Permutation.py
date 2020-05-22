class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i == -1:
            for k in range(len(nums) / 2):
                nums[k], nums[len(nums) - 1 - k] = nums[len(nums) - 1 - k], nums[k] 
            return
        else:
            j = i + 1
            idx = -1
            diff = float('inf')
            while j < len(nums):
                if nums[j] > nums[i] and nums[j] - nums[i] < diff:
                    idx = j
                    diff = nums[j] - nums[i]
                j += 1

            nums[i], nums[idx] = nums[idx], nums[i]
            nums[i + 1:] = sorted(nums[i + 1:])
            return 
        
    def nextPermutationLong(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        
        inc = True
        dec = True
        
        for i in range(len(nums) - 1):
            inc &= (nums[i] <= nums[i + 1])
            dec &= (nums[i] >= nums[i + 1])
            if not inc and not dec: break
        if inc: 
            nums[-1], nums[-2] = nums[-2], nums[-1]
            return
        
        if dec:
            for i in range(len(nums) / 2):
                nums[i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[i]
            return
        
        # if last 2 digits increasing, swap
        if nums[-1] > nums[-2]:
            nums[-1], nums[-2] = nums[-2], nums[-1]
            return
        else:
            i = len(nums) - 2
            while nums[i] >= nums[i + 1]:
                i -= 1
            j = i + 1
            idx = -1
            diff = float('inf')
            while j < len(nums):
                if nums[j] > nums[i] and nums[j] - nums[i] < diff:
                    idx = j
                    diff = nums[j] - nums[i]
                j += 1
            
            nums[i], nums[idx] = nums[idx], nums[i]
            nums[i + 1:] = sorted(nums[i + 1:])
            return 

        
s = Solution()
a = [1, 1]
# b = [2,3,1]
# c = [1,1]
s.nextPermutation(a)
# s.nextPermutation(b)
# s.nextPermutation(c)
print(a)
