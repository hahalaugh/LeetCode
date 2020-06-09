class Solution(object):

    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return False
        nums.sort()
        peri = sum(nums)
        if peri % 4 != 0:
            return False
        
        edge = peri / 4
        
        s = [0] * 4
        def bc(idx):
            if idx == len(nums):
                return s[0] == s[1] == s[2] == edge

            for i in range(4):
                if s[i] + nums[idx] <= edge:
                    s[i] += nums[idx]
                    #result |= bc(idx+1)
                    if bc(idx+1):
                        return True
                    s[i] -= nums[idx]
            return False

        return bc(0)
    
s = Solution()
print(s.makesquare([1,1,2,2,2]))
