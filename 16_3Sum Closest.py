class Solution(object):
    def threeSumClosest(self, nums, target):
        #排序+2pointer N^2
        #逼近的时候两边不同时靠近以防错过局部最值。
        result = float('inf')
        nums.sort()
        for i in range(len(nums)-1):
            goal = target - nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return target
                elif abs(target-s) < abs(target-result):
                    result = s
                elif target > s:
                    l += 1
                else:
                    r -= 1
        return result
         
    def threeSumClosestTwoPointer(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.result = float('inf')
        self.found = False

        def cal(cur, idx):
            if self.found: 
                return 
            
            if len(cur) == 2:
                for n in nums[idx:]:
                    d = abs(target - sum(cur) - n)
                    if d == 0:
                        self.result = target
                        self.found = True
                        return
                    else:
                        if d < abs(target - self.result):
                            self.result = sum(cur) + n
            else:
                for i in range(idx, len(nums)):
                    cur.append(nums[i])
                    cal(cur, i + 1)
                    cur.pop()
        
        cal([], 0)
        return self.result